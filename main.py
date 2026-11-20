import streamlit as st
import database
import datetime

st.set_page_config(page_title="LJ EVents Sales Tracker",page_icon="📈",layout="wide")

## Making sure the database and table exist
database.create_table()

st.title("📈Event Sales Tracker")
st.caption("Easily keep tabs on your event sales perfomance")

if "message" in st.session_state:
    st.success(st.session_state.pop("message"))
    
sales=database.get_all_sales()

def describe(sale):
    return f"#{sale['id']} - {sale['client_name']}"

tab_view,tab_add,tab_update,tab_delete,tab_profit=st.tabs(["View","Add","Update","Delete","Profit"])

with tab_view:
    st.subheader("All sales")
    if sales:
        st.dataframe(sales, hide_index=True)
        st.write(f"Total:{len(sales)} sale(s)")
    else:
        st.info("No sales.Add them in the add tab")
        
with tab_add:
    st.subheader("Add sales")
    with st.form("add_form",clear_on_submit=True):
        client_name=st.text_input("Name")
        category=st.text_input("Category")
        date=st.date_input("Date",min_value=datetime.date(2024,3,1))
        selling_price=st.number_input("Selling Price",min_value=0.0)
        expenses=st.number_input("Expenses",min_value=0.0)
        submitted=st.form_submit_button("Add sale")
    
    if submitted:
        if client_name.strip() == "":
            st.error("Client name cannot be empty")
        else:
            database.add_sale(
                client_name.strip(),
                category.strip(),
                str(date),
                int(selling_price),
                int(expenses))
            st.session_state["message"] = f"added {client_name.strip()} successfully!"
            st.rerun()
            
            
with tab_update:
    st.subheader("You can update your sales here")
    if sales:
        selected_sale=st.selectbox(
            "Choose a sale",
            sales,
            format_func=describe,
            key="update_choice"
        )
        
        new_client_name = st.text_input("Name", value=selected_sale["client_name"], key=f"client_name{selected_sale['id']}")
        new_category=st.text_input("Category",value=selected_sale["category"],key=f"category{selected_sale["id"]}")
        new_date= st.date_input("Date",value=selected_sale["date"],key=f"date{selected_sale['id']}")
        
        new_selling_price= st.number_input(
            "Selling_price",
            value=float(selected_sale["selling_price"]),
            min_value=0.0,
            step= 1.0,
            key=f"selling_price{selected_sale['id']}")
        
        new_expenses=st.number_input(
            "New_expenses",
            value=float(selected_sale["selling_price"]),
            min_value=0.0,
            step=1.0,
            key=f"expenses{selected_sale["id"]}"
            )
        
        if st.button("Save changes"):
            if new_client_name.strip()== "":
                st.error("Client name can't be empty")
            else:
                database.update_sale(
                    selected_sale["id"],
                    new_client_name.strip(),
                    new_category.strip(),
                    str(new_date),
                    int(new_selling_price),
                    int(new_expenses)
                )
                
            st.session_state["message"]=f"Updated {client_name.strip()} successfully!"
            st.rerun  
    else:
        st.info("There is no new client to update")
        
with tab_delete:
    st.subheader("Delete a wrongly placed sale")
    if not sales:
        st.info("There is no sale to delete")
    else:
        if sales:
                sale_to_delete=st.selectbox(
                    "Choose a sale",
                    sales,
                    format_func=describe,
                    key="delete_choice"
                )
                sure=st.checkbox(f"Yes,I want to delete this sale")
                if st.button("Delete",type="primary",disabled=not sure):
                    database.delete_sale(sale_to_delete["id"])
                    st.session_state["message"]=f"Deleted {sale_to_delete['client_name']} successfully!"
                    st.rerun()
with tab_profit:
    st.subheader("Profit by Category")

    if not sales:
        st.info("No sales recorded yet")
    else:
        category_summary = {}   

    for s in sales:# Group blank categories under "Uncategorized" and clean up casing
            cat = s["category"].strip().title() or "Uncategorized"
            profit = s["selling_price"] - s["expenses"]

            if cat not in category_summary:
                category_summary[cat] = {
                    "Category": cat,
                    "Sales Count": 0,
                    "Revenue": 0,
                    "Expenses": 0,
                    "Profit": 0,
                }

            category_summary[cat]["Sales Count"] += 1
            category_summary[cat]["Revenue"] += s["selling_price"]
            category_summary[cat]["Expenses"] += s["expenses"]
            category_summary[cat]["Profit"] += profit

# Convert dictionary values to a list sorted by highest profit first
    category_rows = sorted(
            category_summary.values(),
            key=lambda x: x["Profit"],
            reverse=True
        )

    st.dataframe(
        category_rows, 
        hide_index=True, 
        use_container_width=True)

