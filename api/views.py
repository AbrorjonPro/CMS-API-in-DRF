
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.conf import settings
from .serializers import *
from .models import *
from .permissions import editing_object
from django.core.mail import send_mail
from decouple import config
from .paginations import LargeResultsSetPagination, StandardResultsSetPagination
from docx import Document
import json
from datetime import datetime

class WhyUsView(ModelViewSet):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:  # editing_object(request)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = WhyUs.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class FAQView(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
 

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(FAQ.objects.all(), many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class FrontPagesView(ModelViewSet):
    queryset = FrontPages.objects.all()
    serializer_class = FrontPagesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = FrontPages.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class FrontStatisticsView(ModelViewSet):
    queryset = FrontStatistics.objects.all()
    serializer_class = FrontStatisticsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = FrontStatistics.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    queryset = None
    permission_classes = (AllowAny,)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.validated_data.get("email")
                user = User.objects.get(email=email)
                try:
                    VerificationCode.objects.filter(email=email).delete()
                except:
                    pass
                user_code = VerificationCode.objects.create(email=email)
                user_code.save()
                subject = "Account Verification Message"
                message = f"""
                        Assalomu alaykum, {email}.\n
                        Somebody tried to reset password of your account as {user.first_name} {user.last_name}.\n
                        Here, We have sent a confirmation code to you for authorization if it's really you.\n 
                        Confirmation Code: {user_code.code} \n
                        Please, DON'T GIVE THIS CODE ANYONE. \n
                        Thanks for being with codecraft.uz
                    """
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=config("EMAIL_USER", default=""),
                    recipient_list=[email],
                    fail_silently=True,
                )
                return Response(
                    {"detail": f"Verification code sent to {email}."}, status=200
                )
            except Exception as e:
                return Response({"detail": f"{e}"}, status=400)
        return Response(serializer.errors, status=400)


class PasswordResetConfirmView(APIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            code = serializer.validated_data.get("code")
            new_password1 = serializer.validated_data.get("new_password1")
            new_password2 = serializer.validated_data.get("new_password2")
            try:
                user = User.objects.get(email=email)
                user_code = VerificationCode.objects.filter(email=email).last()
                if user_code.code == code:
                    if new_password1 == new_password2:
                        user.set_password(new_password1)
                        user.save()
                        user_code.delete()
                        return Response(
                            {"detail": "Password has been successfully set."},
                            status=200,
                        )
                    return Response(
                        {
                            "detail": "Password and Password confirmations fields doesn't equal to each other."
                        },
                        status=400,
                    )
                else:
                    return Response(
                        {
                            "detail": "Verification Code is not compatible. Please get new."
                        },
                        status=400,
                    )
            except Exception as e:
                return Response({"detail": f"{e}."}, status=400)
        return Response(serializer.errors, status=400)


class CoursesView(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = Courses.objects.all()
        serializer = CoursesListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=200)


    def create(self, request, *args):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return Response({"detail": "You haven't got this permission"}, status=403)


    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class PricesView(ModelViewSet):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = Prices.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class ActionsView(ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = Actions.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def list(self, request, *args, **kwargs):
        queryset = Contact.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            object = self.get_object()
            serializer = self.serializer_class(object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return Response({"detail": "You haven't got this permission"}, status=403)

    def delete(self, request):
        try:
            if request.user.is_staff:
                object = self.get_object()
                object.delete()
                return Response({"detail": "Successfully deleted."}, status=200)
            return Response({"detail": "You haven't got this permission"}, status=403)
        except Exception as e:
            return Response({"detail": f"{e}"}, status=400)


class AllDataView(ModelViewSet):
    queryset = FrontPages.objects.all()
    serializer_class = FrontPagesSerializer

    permission_classes = (IsAuthenticatedOrReadOnly,)
    allowed_methods = (
        "GET",
        "HEAD",
    )

    def list(self, request):
        data = {}
        data["front_statistics"] = FrontStatisticsSerializer(
            FrontStatistics.objects.all(), many=True
        ).data
        data["front_pages"] = FrontPagesSerializer(
            FrontPages.objects.all(), many=True
        ).data
        data["FAQ"] = FAQSerializer(FAQ.objects.all(), many=True).data
        data["WhyUs"] = WhyUsSerializer(WhyUs.objects.all(), many=True).data
        return Response(data, status=200)


class CallOrdersView(ModelViewSet):
    """
    This is an API for creating and listing Call Orders by Clients
    """

    queryset = Call_orders
    serializer_class = CallOrderSerializer
    permission_classes = (AllowAny,)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def list(self, request):
        if request.user.is_staff:
            serializer = self.serializer_class(Call_orders.objects.all(), many=True)
            return Response(serializer.data, status=200)
        return Response(
            {"detail": "You have not permission for this action."}, status=403
        )

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        except:
            return Response(serializer.errors, status=400)

    def delete(self, request):
        object = self.get_object()
        try:
            if request.user.is_staff:
                object.delete()
                return Response({"detail": "Object was deleted. "}, status=200)
            return Response(
                {"detail": "You have not permission for this action."}, status=403
            )
        except:
            return Response({"detail": "Bad Request"}, status=400)


class TimeSlotsView(ModelViewSet):
    queryset = Timeslots.objects.all()
    serializer_class = TimeslotsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    

class AdminGroupsView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self, c=None, ts=None, archives=False, all=False):
        if all:
            queryset = Group.objects.all()
        elif archives:
            queryset = Group.objects.get_archive_groups()
        elif c:
            queryset = Group.objects.get_active_groups().filter(course_id=int(c))
        elif ts:
            queryset = Group.objects.get_active_groups().filter(timeslot_id=int(ts))
        else:
            queryset = Group.objects.get_active_groups()
        return queryset

    def list(self, request, *args, **kwargs):
        course = request.query_params['c'] if ('c' in request.query_params.keys()) else None
        timeslot = request.GET.get('ts', None)
        archives = request.GET.get('archives', False)
        all = request.GET.get('all', False)
        queryset = self.get_queryset(c=course, ts=timeslot, archives=archives, all=all)
        print(queryset.count())
        serializer = GroupsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        object = get_object_or_404(Group, pk=kwargs['pk'])
        serializer = self.serializer_class(object, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class AdminGroupStudentsView(ModelViewSet):
    queryset = Group_Students.objects.all()
    serializer_class = GroupStudentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    
    def list(self, request):
        if request.query_params and 'gr' in request.query_params.keys():
            queryset = self.queryset.filter(group_id=int(request.query_params['gr']))
            serializer = GroupStudentsListSerializer(queryset, many=True,context={'request': request})
            return Response(serializer.data, status=200)
        elif request.query_params and 'i' in request.query_params.keys():
            groups = GroupInstructors.objects.filter(instructor__first_name=request.query_params['i'])
            queryset = list(map(lambda group: self.queryset.filter(group=group), groups))
            serializer = self.serializer_class(queryset, many=True,context={'request': request})
            return Response(serializer.data, status=200)
        else:
            now = datetime.now()
            g_students = Group_Students.objects.all()
            serializer = GroupStudentsListSerializer(g_students, many=True,context={'request': request})
            return Response(serializer.data, status=200)

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Parenting_studentsViews(ModelViewSet):
    queryset = Parenting_students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    
    def list(self, request):
        serializer = StudentsListSerializer(self.queryset, many=True, context={'request':request})
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk, *args, **kwargs):
        try:
            student = User_data.objects.get(id=pk)
            object = Parenting_students.objects.get(student=student)
        except:
            object = Parenting_students.objects.get(id=pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

    
class UserView(ModelViewSet):
    queryset = User_data.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self, position=None):
        if position:
            try:
                natija = User_data.objects.filter(position=position)
                return natija
            except Exception as e:
                raise e
                
        else:
            return User_data.objects.all()

    def list(self, request):
        if request.query_params and "only" in request.query_params.keys():
            serializer = UserDataListSerializer(User_data.objects.filter(position=request.query_params["only"]), many=True, context={'request': request})
        else:
            serializer = UserDataListSerializer(self.get_queryset(), many=True, context={'request': request})
        return Response(serializer.data, status=200)

class AdminUserPasswordChangeView(APIView):
    queryset = User_data.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserPasswordChangeSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get('user_id')
            password = serializer.validated_data.get('password')
            try:
                user = get_object_or_404(User_data, pk=user_id)
                user.set_password(raw_password=password)
                user.save()
                return Response({'status':'ok', 'message':'password changed succesfully.'}, status=200)
            except Exception as e:
                raise e
    
class InstructorView(ModelViewSet):
    queryset = User_data.objects.filter(position="i")
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request, *args, **kwargs):
        serializer = UserDataListSerializer(self.queryset, many=True, context={'request':request})
        return Response(serializer.data, status=200)

    # parser_classes = (JSONParser, MultiPartParser, FormParser,)
    # http_allowed_methods = ('GET', 'OPTIONS', 'HEAD')

class AdminsView(ModelViewSet):
    queryset = User_data.objects.filter(position="a")
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = (JSONParser, MultiPartParser, FormParser,)
    # http_allowed_methods = ('GET', 'OPTIONS', 'HEAD')

class CompanyDataView(ModelViewSet):
    queryset = Company_Data.objects.all()
    serializer_class = Company_DataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = (JSONParser, MultiPartParser, FormParser,)


class PaymentsView(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = (JSONParser, MultiPartParser, FormParser,)

class GroupInstructorsView(ModelViewSet):
    queryset = GroupInstructors.objects.all()
    serializer_class = GroupInstructorsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = (JSONParser, MultiPartParser, FormParser,)
    
    def list(self, request, *args, **kwargs):
        if request.query_params and 'i' in request.query_params.keys():
            queryset = self.queryset.filter(instructor_id=int(request.query_params['i']))
        else:
            queryset=self.queryset
        serializer = GroupInstructorsListSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data, status=200)


class GroupStudentCreateView(ModelViewSet):
    serializer_class = StudentIDSerializer
    queryset = StudentGroupModels.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = (JSONParser, MultiPartParser, FormParser,)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            student_id = serializer.validated_data.get("student_id")
            student = User_data.objects.get(id=student_id)
            group = serializer.validated_data.get("group")
            company_data = Company_Data.objects.all()
        contract_data = {}
        for comp_data in company_data:
            contract_data[comp_data.data_field] = comp_data.value
        if student.position=="s":
            try:
                parent = Parenting_students.objects.get(student=student).parent
                if parent is not None:
                    parent=parent
                else:
                    parent = student
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
            group_student = Group_Students.objects.create(
                student=student, 
                group=group, 
                contract=contract, 
                )
            new_serializer = GroupStudentsSerializer(group_student, many=False)
            return Response(new_serializer.data, status=200)
        return Response(serializer.errors, status=400)
  

class CompanyArchivesView(ModelViewSet):
    queryset = CompanyArchives.objects.all()
    serializer_class = CompanyArchivesSerializer
    # parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        

class RebatesView(ModelViewSet):
    queryset = Rebate.objects.all()
    serializer_class = RebateSerializer
    permission_classes = (IsAuthenticated, )



class PaymentsView(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsCreateSerializer
    permission_classes = (IsAuthenticated, )


    def list(self, request, *args, **kwargs):
        if request.query_params and request.query_params['m']:
            try:
                queryset = Payments.objects.filter(for_month=request.query_params['m'])
            except Exception as e:
                return Response({'detail':f'{e}'}, status=400)
        else:
            queryset = Payments.objects.all()
        serializer = PaymentsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=200)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.error, status=400)


