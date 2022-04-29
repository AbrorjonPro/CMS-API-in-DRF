from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api'

router = DefaultRouter()
####### Only for frontend (client panel view)
router.register(r'faq', FAQView)
router.register(r'faq/<int:pk>', FAQView)
router.register(r'why-us', WhyUsView)
router.register(r'why-us/<int:pk>', WhyUsView)
router.register(r'front-pages', FrontPagesView)
router.register(r'front-pages/<int:pk>', FrontPagesView, basename="front-pages-detail")
router.register(r'front-statistics', FrontStatisticsView, basename="Front-statistics")
router.register(r'front-statistics/<int:pk>', FrontStatisticsView, basename="Front-statistics-detail")

router.register(r'courses', CoursesView)
# router.register(r'courses/<slug:slug>', CoursesView, basename="courses-detail")
router.register(r'prices', PricesView, basename="prices")
router.register(r'actions', ActionsView, basename="actions")
router.register(r'contact', ContactView, basename="contact")
router.register(r'all-data', AllDataView, basename="all-data")
router.register(r'call-ordering', CallOrdersView, basename="call-ordering")


router.register(r"time-slots", TimeSlotsView)
router.register(r'groups', AdminGroupsView)
router.register(r'group-students', AdminGroupStudentsView)
router.register(r'students', Parenting_studentsViews) 
router.register(r'instructors', InstructorView)
router.register(r'admins', AdminsView)
router.register(r'users', UserView)
router.register(r'company-data', CompanyDataView)
router.register(r'payments', PaymentsView)
router.register(r'group-instructors', GroupInstructorsView)
router.register(r'group-student-create', GroupStudentCreateView)
router.register(r'rebates', RebatesView)
router.register(r'payments', PaymentsView)


urlpatterns = [
    path('users/password/change/', AdminUserPasswordChangeView.as_view(), name='password_change_view_by_admins'),
]
urlpatterns += router.urls
