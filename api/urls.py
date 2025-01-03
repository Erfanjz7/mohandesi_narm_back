from django.urls import path

from api.views import (
    AcceptAnOrderAPIView,
    AddFoodAPIView,
    AddToCartAPIView,
    CreateOrderAPIView,
    DeleteFoodAPIView,
    EmployeesAPIView,
    FoodDetailAPIView,
    LoginAPIView,
    ShowAcceptedOrdersAPIView,
    ShowCartAPIView,
    ShowFoodsListAPIView,
    ShowOrderAPIView,
    ShowPendingOrdersAPIView,
    UpdateFoodAPIView,
    LogoutAPIView,
    RgisterCustomerAPIView,
    GetCategoriesAPIView,
    DeleteFromCartAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view() , name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("signup/", RgisterCustomerAPIView.as_view(), name="signup"),
    path("foods/list/", ShowFoodsListAPIView.as_view(), name="show_foods"),
    path("food/detail/<int:id>/", FoodDetailAPIView.as_view(), name="food_detail"),
    path("food/add-to-cart/", AddToCartAPIView.as_view(), name="add_to_cart"),
    path("food/delete-from-cart/<int:id>/",DeleteFromCartAPIView.as_view(),name="delete_from_cart"),
    path("cart/", ShowCartAPIView.as_view(), name="my_cart"),
    path("createorder/",CreateOrderAPIView.as_view(), name="create_order"),
    path("orders/", ShowOrderAPIView.as_view(), name="my_order"),
    path("employee/orders/pending/", ShowPendingOrdersAPIView.as_view(), name="pending_orders"),
    path("employee/orders/accepted/", ShowAcceptedOrdersAPIView.as_view(), name="accepted_orders"),
    path("employee/orders/accept/<int:id>/", AcceptAnOrderAPIView.as_view(), name="accept_order"),
    path("admin/food/add/", AddFoodAPIView.as_view(), name="add_food"),
    path("admin/food/<int:id>/edit/", UpdateFoodAPIView.as_view(), name="update_food"),
    path("admin/food/<int:id>/delete/", DeleteFoodAPIView.as_view(), name="delete_food"),
    path("admin/employee/register/", EmployeesAPIView.as_view(), name="register_employee"),
    path("admin/employees/", EmployeesAPIView.as_view(), name="show_employees"),
    path("admin/employee/delete/<int:id>/", EmployeesAPIView.as_view(), name="delete_employee"),
    path("admin/employee/edit/<int:id>/", EmployeesAPIView.as_view(), name="edit_employee"),
    path("getcategories/", GetCategoriesAPIView.as_view(), name="get_categories")
]
