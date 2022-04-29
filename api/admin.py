from django.contrib import admin
from .models import *
from import_export import resources, admin as ie_admin


class PaymentsInline(admin.StackedInline):
    model = Payments
    fk_name = 'student'
    classes = ('collapse',)

class GroupInstructorsInline(admin.StackedInline):
    model = GroupInstructors
    classes = ('collapse',)

class AddToGroupInline(admin.StackedInline):
    model = Group_Students
    classes = ('collapse',)

class ParentInline(admin.StackedInline):
    model = Parenting_students
    fk_name = 'student'
    max_num = 1
    classes = ('collapse',)


class StudentInline(admin.StackedInline):
    model = Parenting_students
    fk_name = 'parent'
    max_num = 1
    classes = ('collapse',)

class User_dataResource(resources.ModelResource):
    class Meta:
        model = User_data

class User_dataAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = User_dataResource
    list_display = ("first_name", "last_name", "patronymic", "position",)
    list_filter = ("position", "blocked", "deleted")
    list_editable = ("position",)
    search_fields = ("id", "first_name", "last_name")

    fieldsets = (
        ('Login INFOS', {
            'fields':('username', 'password','position'),
        }),
        ('USER MAIN INFOS', {
            'fields':(('first_name', 'last_name'),'patronymic', 'birthdate', ),
            'classes':('collapse',)
        }),
        ('LEGAL_PASSWORD INFOS', {
            'fields':('passport_address', ('passport_number', 'passport_serial'), ('passport_who_give', 'passport_when_give'))
        }),
        ('PERMISSIONS', {
            'fields':(('is_superuser', 'is_staff', 'is_active'), 'user_permissions',),
            'classes':('collapse'),
        })
    )
    filter_horizontal = ('user_permissions', )

    inlines = [ParentInline, StudentInline, AddToGroupInline]

admin.site.register(User_data, User_dataAdmin)


admin.site.register(School_branches)


class TimeSlotsResource(resources.ModelResource):
    class Meta:
        model = Timeslots

class TimeSlotsAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = TimeSlotsResource
    list_display = ("id", "timeslot_name", "start_time", "end_time", "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    list_editable = ("timeslot_name", "start_time", "end_time", "mon", "tue", "wed", "thu", "fri", "sat", "sun")


admin.site.register(Timeslots, TimeSlotsAdmin)
admin.site.register(Call_orders)


class CoursesResource(resources.ModelResource):
    class Meta:
        model = Courses

class CoursesAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ("short_title",)
    list_display = ("short_title", "price",)
    list_editable = ("price",)
    prepopulated_fields = {"slug":("short_title", )}
    resource_class = CoursesResource
    


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Courses_Slugs)
admin.site.register(Course_Sections)

class Company_DataResource(resources.ModelResource):
    class Meta:
        model = Company_Data

class Company_DataAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = Company_DataResource


admin.site.register(Company_Data, Company_DataAdmin)
admin.site.register(Classrooms)
admin.site.register(Courses_Slugs_id)

class Company_DataResource(resources.ModelResource):
    class Meta:
        model = Company_Data

class Company_DataAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = Company_DataResource


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
class GroupAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = GroupResource
    search_fields = ("course__short_title","timeslot__timeslot_name")
    list_display = ("course", "timeslot", "start_date", "end_date", "finished",)

admin.site.register(Group, GroupAdmin)


class Group_StudentsResource(resources.ModelResource):
    class Meta:
        model = Group_Students
class Group_StudentsAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = Group_StudentsResource
    search_fields = ("student__first_name", "group__id", "id","contract_no", )
    list_display = ("student", "group_id", "id","contract_no")

admin.site.register(Group_Students, Group_StudentsAdmin)


class GroupInstructorsResource(resources.ModelResource):
    class Meta:
        model = GroupInstructors
class GroupInstructorsAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):  #, admin.StackedInline
    # model = GroupInstructors
    # extra=0
    # ordering = ("-id")
    resource_class = GroupInstructorsResource
    search_fields = ("id", "instructor__id", "instructor__first_name", "group__id",)
    list_display = ("id", "instructor", "group")
    list_filter = ("instructor", "group")
    
admin.site.register(GroupInstructors, GroupInstructorsAdmin)


admin.site.register(Prereq)


class PaymentsResource(resources.ModelResource):
    class Meta:
        model = Payments
class PaymentsAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = PaymentsResource
admin.site.register(Payments, PaymentsAdmin)


class Parenting_studentsResource(resources.ModelResource):
    class Meta:
        model = Parenting_students
class Parenting_studentsAdmin(ie_admin.ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = Parenting_studentsResource
    search_fields = ("id", "student__first_name","parent__first_name", "student__last_name", "parent__last_name")
admin.site.register(Parenting_students, Parenting_studentsAdmin)
admin.site.register(FAQ)
admin.site.register(FrontPages)
admin.site.register(FrontStatistics)
admin.site.register(WhyUs)


class PricesAdmin(admin.ModelAdmin):
    list_display = ("course_type", "USD", "UZS", "RUBL", "EUR")

admin.site.register(Prices)
admin.site.register(CompanyArchives)


class RebateAdmin(admin.ModelAdmin):
    list_display = ("student", "rebate", "for_month", "date_added",)
    search_fields = ("student", "rebate", "for_month", "date_added",)
    list_filter = ("rebate", "for_month")

admin.site.register(Rebate, RebateAdmin)
