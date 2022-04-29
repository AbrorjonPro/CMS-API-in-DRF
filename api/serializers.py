from docx import Document
from .models import *
from rest_framework import serializers
from django.conf import settings
from django.core.files.base import ContentFile
from datetime import datetime, timedelta
import json
from django.core import serializers as json_serializers
class VerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = "__all__"


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=10)
    new_password1 = serializers.CharField(max_length=100)
    new_password2 = serializers.CharField(max_length=100)

    class Meta:
        fields = ("email", "code", "new_password1", "new_password2")
        extra_kwargs = {
            "new_password1": {"write_only": True},
            "new_password2": {"write_only": True},
        }



class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class FrontPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontPages
        fields = "__all__"


class FrontStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontStatistics
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class UserDataListSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user_data-detail", lookup_field='pk')
    class Meta:
        model = User_data
        fields = ("url", "first_name", "last_name", "patronymic", "position", "id")



class  UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ("id", "username", "first_name", "last_name","password",  "patronymic", "birthdate", "is_staff", "is_superuser",
            "email", "is_active", "individual_type", "blocked", "notes", 
            "profile_photo", "position", "phone_number", "extra_phone_numbers", 
            "passport_address", "passport_number", "passport_serial", "passport_who_give",
            "passport_when_give", "passport_file", "passport_file1", #"office_address", "office_bank_account",
            # "office_bank_code", "office_inn", "office_licence_file", "deleted"
            )
        extra_kwargs = {
            # 'username':{'write_only':True},
            'email':{'read_only':True},
            'date_joined':{'read_only':True},
            'last_login':{'read_only':True},
            'user_permissions':{'read_only':True},
            # 'groups':{'read_only':True},
            'password': {'write_only': True, },
            'last_login': {'read_only': True, },
            # 'blocked': {'read_only': True, },
            'deleted': {'read_only': True, },
            # 'groups': {'read_only': True, },
            'user_permissions': {'read_only': True, },
            'is_superuser': {'write_only': True, },
            'is_staff': {'write_only': True, },
            'is_active': {'write_only': True, },
        }


class UserPasswordChangeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField()

    class Meta:
        fields = ('user_id', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
        # lookup_field = "slug"

class CoursesForOtherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ("url", "id", "short_title")
        extra_kwargs = {
            "url":{"view_name":"api:courses-detail", "lookup_field":"pk"}
        }



class GroupsListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")
    class Meta:
        model = Group
        fields = ("url", "name", "id")
        # depth=1
 
class CoursesListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:courses-detail")
    get_groups = GroupsListSerializer(many=True)
    class Meta:
        model = Courses
        fields = ("url", "id", "short_title", "price", "get_groups", "publicized", "title")
        extra_kwargs = {
            "get_groups":{"read_only":True},
        }


# timeslots serializer
class TimeslotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslots
        fields = "__all__"

class TimeslotsListSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:timeslots-detail")
    class Meta:
        model = Timeslots
        fields = ("url", "timeslot_name", "id","start_time", "end_time")
        depth=1
#group serializers
class GroupsListSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    course = CoursesForOtherSerializer(required=False)
    timeslot = TimeslotsListSerializer()
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")
    class Meta:
        model = Group
        fields = ("url", "course", "name", "timeslot", "start_date", "end_date", "finished",)
        # depth=1

class GroupsForOtherSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    course = CoursesForOtherSerializer(required=False)
    # timeslot = TimeslotsListSerializer()
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")
    get_instructor =  UserDataListSerializer(required=False, many=True)
    class Meta:
        model = Group
        fields = ("url", "id", "course", "name", "get_instructor",)
        # depth=1


class GroupStudentsListSerializer(serializers.ModelSerializer):
    student = UserDataListSerializer(required=False)
    # url = serializers.HyperlinkedIdentityField(view_name="group_students_detail")
    class Meta:    

        model = Group_Students
        fields = ("id","student", "contract", "contract_no")
        
        extra_kwargs = {
            "contract":{"read_only":True},
            "contract_no":{"read_only":True}
        }
class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    course = CoursesForOtherSerializer(required=True)
    timeslot = TimeslotsListSerializer(required=False)
    get_group_students = GroupStudentsListSerializer(required=False, many=True)
    get_instructor = UserDataListSerializer(required=False, many=True)
    class Meta:
        model = Group
        fields = ( "name", "id", "course", "timeslot", "start_date", "end_date", "classroom_building", "classroom_room", "finished","get_instructor", "get_group_students")
        depth=1
        # extra_kwargs = {
        #     'url':{'view_name':'api:group', 'lookup_field':'id'}
        # }

class GroupsCreateSerializer(serializers.ModelSerializer):
    get_group_students = GroupStudentsListSerializer(required=False, many=True)
    get_instructor = UserDataListSerializer(required=False, many=True)
    class Meta:
        model = Group
        fields = ("name", "course", "timeslot", "start_date", "end_date", "classroom_building", "classroom_room", "finish", "activate_again", "get_instructor", "get_group_students")

        extra_kwargs = {
            "get_group_students":{"read_only":True}
        }


#group students serializers
class GroupStudentsListSerializer( serializers.ModelSerializer):
    student = UserDataListSerializer(required=False)
    # url = serializers.HyperlinkedIdentityField(view_name="group_students_detail")
    class Meta:    

        model = Group_Students
        fields = ("id","student", "group", "contract", "contract_no")
        
        extra_kwargs = {
            "contract":{"read_only":True},
            "contract_no":{"read_only":True}
        }

class GroupStudentsSerializer(serializers.ModelSerializer):
    student = UserDataSerializer(required=False)
    group = GroupsForOtherSerializer()
    class Meta:
        model = Group_Students
        fields = "__all__"
        extra_kwargs = {
            "contract":{"read_only":True},
            "contract_no":{"read_only":True}
        }

    def create(self, validated_data):
        student = validated_data["student"]
        group = validated_data["group"]
        certificate = validated_data["certificate"]
        points = validated_data["points"]
        discount = validated_data["discount"]
        company_data = Company_Data.objects.all()
        contract_data = {}
        for comp_data in company_data:
            contract_data[comp_data.data_field] = comp_data.value
        if student.position=="s":
            try:
                parent = Parenting_students.objects.get(student=student).parent
            except:
                parent = student
            if parent.full_name:
                contract_data["parent_full_name"] = parent.full_name
            if parent.passport_serial:
                contract_data["passport_serial"] = parent.passport_serial
            if parent.passport_number:
                contract_data["passport_number"] = parent.passport_number
            if parent.passport_who_give:
                contract_data["passport_who_give"] = parent.passport_who_give
            if parent.passport_when_give:
                contract_data["passport_when_give"] = parent.passport_when_give
            if parent.passport_address:
                contract_data["passport_address"] = parent.passport_address
            if parent.phone_number:
                contract_data["parent_phone_number"] = parent.phone_number
            if student.full_name:
                contract_data["student_full_name"] = student.full_name
            if student.individual_type:
                contract_data["price"] = str(group.course.price)
            else:
                contract_data["price"] = str(group.course.price)
            if student.birthdate:
                contract_data["b_year"] = f"{student.birthdate.year}"
            now = datetime.now()

            contract_data["day"] = "0"+str(now.day) if now.day<10 else str(now.day)
            contract_data["month"] = "0"+str(now.month) if now.month<10 else str(now.month)
            contract_data["cur_year"] = str(now.year)
            contract_data["hours"] = str(int(group.course.lessons)*2)
            contract_data["short_title"] = group.course.short_title
            contract_data["last_contract_no"] = str(int(contract_data["last_contract_no"])+1)
            contract = generate_contract_file(contract_data=contract_data)
            contract_no = contract_data["contract_serial"]+Company_Data.objects.get(data_field="last_contract_no").value
            return Group_Students.objects.create(
                student=student, 
                group=group, 
                contract=contract, 
                certificate=certificate,
                points=points,
                discount=discount,
                contract_no=contract_no
                )
        else:
            raise Exception("Not valid")


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = "__all__"


class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class CallOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call_orders
        fields = "__all__"





class StudentsListSerializer(serializers.HyperlinkedModelSerializer):
    parent = UserDataListSerializer(many=False, required=False, read_only=False)
    student = UserDataListSerializer(many=False, required=False, read_only=False)
    url = serializers.HyperlinkedIdentityField(view_name="api:parenting_students-detail")
    class Meta:
        model = Parenting_students
        fields = ['url', 'parent', 'student']

class StudentSerializer(serializers.ModelSerializer):
    parent = UserDataSerializer(many=False, required=False, read_only=False)
    student = UserDataSerializer(many=False, required=False, read_only=False)
    class Meta:
        model = Parenting_students
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        parent_user = None
        student_user = None
        parenting = None
        parent=validated_data.pop("parent")
        if 'student' in validated_data:
            student=validated_data.pop("student")
            student_user= User_data.objects.create(
                first_name=student["first_name"], last_name=student["last_name"],
                patronymic=student["patronymic"], password="testing321",
                birthdate=student["birthdate"], phone_number=student["phone_number"], extra_phone_numbers=student["extra_phone_numbers"],
                is_staff=False,
                position="s", notes=student["notes"], blocked=False,
                individual_type=student["individual_type"],
                passport_address=student["passport_address"], passport_number=student["passport_number"],
                passport_serial=student["passport_serial"],
                passport_who_give=student["passport_who_give"], passport_when_give=student["passport_when_give"],
                passport_file=student["passport_file"],
                passport_file1=student["passport_file1"], 
            )  
            # student_user.set_password(f"{student['password']}")
            student_user.save()
        if parent["first_name"]!='' and parent["last_name"] != '':
            parent_user = User_data.objects.create(
                first_name=parent["first_name"], last_name=parent["last_name"],
                patronymic=parent["patronymic"], password="testing321",
                birthdate=parent["birthdate"], phone_number=parent["phone_number"], extra_phone_numbers=parent["extra_phone_numbers"],
                is_staff=False,
                position="p", notes=parent["notes"], blocked=False,
                individual_type=parent["individual_type"],
                passport_address=parent["passport_address"], passport_number=parent["passport_number"],
                passport_serial=parent["passport_serial"],
                passport_who_give=parent["passport_who_give"], passport_when_give=parent["passport_when_give"],
                passport_file=parent["passport_file"],
                passport_file1=parent["passport_file1"],
            )
            parent_user.save()
        
        # if parent_user is not None and student_user is not None:
        
        parenting = Parenting_students.objects.create(student=student_user, parent=parent_user)
        return parenting
    
    def update(self, instance, validated_data):
        if 'student' in validated_data:
            student = validated_data.get('student')
            student_serializer = self.fields['student']
            student_instance = instance.student
            student_serializer.update(student_instance, student)
        if 'parent' in validated_data and instance.parent is not None:
            parent = validated_data.get('parent')
            parent_serializer = self.fields['parent']
            parent_instance = instance.parent
            parent_serializer.update(parent_instance, parent)
        instance.save()
        return instance


class StaffRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = "__all__"


class Company_DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Data
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

class GroupInstructorsListSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    group = GroupsListSerializer(required=False)
    instructor = UserDataListSerializer(required=False)
    url = serializers.HyperlinkedIdentityField(view_name="api:groupinstructors-detail")
    class Meta:
        model = GroupInstructors
        fields = ('url', "group", "instructor", "id",)
        depth = 1


class GroupInstructorsSerializer(serializers.ModelSerializer):
    group = GroupsSerializer(required=False)
    instructor = UserDataSerializer(required=False)
    
    class Meta:
        model = GroupInstructors
        fields = "__all__"
        depth = 1

    # def create(self, validated_data):
    #     instructor = validated_data["instructor"]
    #     group = validated_data["group"]
    #     instructor_object = User_data.objects.create(**instructor)
    #     group = Group.objects.create(**group)

class StudentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroupModels
        fields = "__all__"


def get_archives(date_start=None, date_end=None):
    students = User_data.objects.filter(date_joined__gte=date_start, date_joined__lte=date_end, position="s")
    now=datetime.now()


    groups = Group.objects.filter(finished__gte=date_start, finished_lte=date_end)
    filename=f"{now.month}_{now.year}.json"
    archive_file=open(filename, "w")
    for student in students:
        data = {}
        try:            
            date_student = serializers.serialize(students, fields=("id", "last_name", "first_name", "patronymic", "birthdate", "phone_number", "position", "individual_type", "passport_address", "passport_number", "passport_serial", "passport_who_give", "passport_when_give", "create_date", "update_date"))
        except Exception as e:
            date_student = students            
            data_contract = serializers.serialize(Group_Students.objects.get(student=student),fields=("contract_no"))
            data_parent = serializers.serialize(Parenting_students.objects.get(student=student).parent, fields=("id", "last_name", "first_name", "patronymic", "birthdate", "phone_number", "position", "individual_type", "passport_address", "passport_number", "passport_serial", "passport_who_give", "passport_when_give", "create_date", "update_date"))
            data_payment = serializers.serialize(Payments.objects.get(student=student))
        
    
    students_json = serializers.serialize(students, fields=("id", "last_name", "first_name", "patronymic", "birthdate", "phone_number", "position", "individual_type", "passport_address", "passport_number", "passport_serial", "passport_who_give", "passport_when_give", "create_date", "update_date"))
    json_file = json.loads(students_json)
    json.dump(json_file, archive_file, ensure_ascii=False, indent=4)





class CompanyArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyArchives
        fields = "__all__"
        extra_kwargs = {
            "file":{"read_only":True},
            "admin":{"read_only":True},
            "date_archived":{"read_only":True}
        }
    
    def create(self, validated_data):
        admin = self.context["request"].user.full_name
        date_start = validated_data["date_start"]
        date_end = validated_data["date_end"]
        file = get_archives(date_start, date_end)
        name = f"archieved_data_by {admin} at {datetime.now()}"
        return CompanyArchives.objects.create(
                name=name,
                admin=admin, 
                date_start=date_start,
                date_end=date_end,
                file=file
            )
            


class RebateSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:rebate-detail")
    student = UserDataListSerializer()
    group = GroupsListSerializer(required=False)
    class Meta:
        model = Rebate
        fields = ('url', 'student', 'group', 'rebate', 'notes', 'for_month', 'date_added')

        extra_kwargs = {
            'url':{'lookup_field':'url'},
            'date_added':{'read_only':True}
        }


class PaymentsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:payments-detail", lookup_field='pk')
    parent = UserDataListSerializer()
    group = GroupsListSerializer()
    student = UserDataListSerializer()


    class Meta:
        model = Payments
        fields = "__all__"   #('student', 'parent', 'group','amount', 'date_time', 'for_month', 'admin', 'paid')


class PaymentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('student', 'group', 'payment_method', 'amount', 'for_month', 'notes', 'paid')
