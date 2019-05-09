from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [

    # bayi yönetimi sayfaları | distributor
    path('dealer/create/', views.DealerCreateView.as_view(), name='create-dealer'),
    path('dealer/edit/<int:pk>/', views.DealerUpdateView.as_view(), name='edit-dealer'),
    path('dealer/delete/<int:pk>/', views.DealerDeleteView.as_view(), name='delete-dealer'),
    path('dealer/list/', views.DealerListView.as_view(), name='list-dealer'),
    path('dealer/attach/', views.DealerRelationView.as_view(), name='attach-dealer'),

    # ürün yönetimi sayfaları | distributor
    path('product/create/', views.ProductCreateView.as_view(), name='create-product'),
    path('product/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit-product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('product/list/', views.ProductListView.as_view(), name='list-product'),

    # shop sayfaları | dealer
    path('shop/list/', views.ShopListView.as_view(), name='list-shop'),
    path('shop/detail/<int:pk>/', views.ShopDetailView.as_view(), name='detail-shop'),
    path('shop/cart/detail/', views.CartView.as_view(), name='detail-cart'),
    path('shop/cart/add/<int:pk>/', views.CartAdd.as_view(), name='add-cart'),
    path('shop/cart/delete/<int:pk>/', views.CartDelete.as_view(), name='delete-cart'),
    path('shop/cart/clear/', views.CartClear.as_view(), name='clear-cart'),

    # sipariş sayfaları | dealer
    path('order/list/', views.OrderListView.as_view(), name='list-order'),
    path('order/detail/<int:pk>/', views.OrderDetailView.as_view(), name='detail-order'),
    path('order/create/', views.OrderAddView.as_view(), name='create-order'),
    path('order/cancel/<int:pk>/', views.OrderDeleteView.as_view(), name='cancel-order'),

    # ödeme sayfaları | dealer

    # sipariş sayfaları | distributor


    # sipariş sayfaları | distributor
    path('distributor/order/list/', views.DistributorOrderListView.as_view(), name='distributor-list-order'),
    path('distributor/order/detail/<int:pk>/', views.DistributorOrderDetailView.as_view(), name='distributor-detail-order'),
    path('distributor/order/approve/<int:pk>/', views.DistributorOrderApproveView.as_view(), name='distributor-create-order'),
    path('distributor/order/cancel/<int:pk>/', views.DistributorOrderDeleteView.as_view(), name='distributor-cancel-order'),


]

