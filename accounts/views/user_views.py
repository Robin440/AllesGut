# Django imports
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Utils imports
from utils.validators import is_valid_email,check_password_for_spaces,is_valid_email,is_valid_password,verify_user
from utils.utils_generator import  generate_random_string,generate_otp
from utils.get_details import get_member,get_member_image

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Models imports
from accounts.models import User,VerificationToken
from member.models import Member,MemberImage,Role
from apps.models import  App,Services


# Serializers import
from member.serializers import MemberCreateSerializers,MemberListSerializers




class LoginView(APIView):
    """
    API view for user login.
    """


    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self, request):

        context = {}

        email = request.data.get("email")
        password = request.data.get("password")

        if not email:
            context["error"] = "Email is required"
            return render(request,'login.html',context)
        if not is_valid_email(email):
            context["error"] = "Invalid email"
            return render(request,'login.html',context)
        
        if not password:
            context["error"] = "Password is required"
            return render(request,'login.html',context)


        if not email or not password:
            return Response({"error": "Email and password are required"}, status=400)

        try:
            user_exist = User.objects.get(email=email)
        except User.DoesNotExist:
            context['error']='User does not exist with this mail'
            return render(request,'login.html',context)
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # User is authenticated, create or get the auth token
            # token, created = Token.objects.get_or_create(user=user)

            # Cchecking if member is associated with any user
            try:
                member = Member.objects.get(user=user)
            except Member.DoesNotExist:
                context['error']='You are not a member'
                return render(request,'login.html',context)

            if member.is_active is False:
                context['error']='Your account is deactivated'
                return render(request,'login.html',context)

            login(request,user)

            try:
                member_image = MemberImage.objects.get(member=member)
                context['image']=member_image.image
            except MemberImage.DoesNotExist:
                member_image = None

            app_list = App.objects.all()

            
            context['user']=user.first_name
            context['apps']=app_list

            print(context)
            return redirect('user_home')
        else:
            context['error']='Invalid email or password'
            return render(request,'login.html',context)

        url_token = generate_random_string()
        context['url_token']=url_token
        return render(request,'login.html',context)


class LogoutAPIView(APIView):
    """
    API for logging out the user
    """
    # permission_classes = [IsAuthenticated]  # Ensures only authenticated users can log out

    def get(self, request):
        # Perform logout
        logout(request)
        context={}
        # Return success response
        context['error']="Logout  successful"
        return render(request,'login.html',context)
        

class HomeListAPIView(APIView):
    """
    API for getting the list of apps
    """
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this API
    def get(self, request,*args,**kwargs):
        """_summary_

        Args:
            request (_type_): _description_
        """
        context = {}
        if not request.user:
            context['error']="User is not authenticated ,please login"
            return render(request,'login.html',context)
        all_apps = App.objects.all()
        serivces = Services.objects.all() 
        app_list = all_apps.filter(is_active=True)
        upcoming_apps = all_apps.filter(up_coming=True)
        user = request.user
        # Accessing member
        try:
            member = get_member(user)
            context['member']=member
        except Exception as e:
            context['error']=f"Member is not generated for this user: {str(e)}"
            return render(request,'home.html',context)

        #  Accessing member's image.
        try:
            member_image = get_member_image(member)
            context['image']=member_image.image
        except:
            pass
        # print(context)
        serializer = MemberListSerializers(member)
        data = {'data':serializer.data,
                'apps':app_list,
                'upcoming_apps':upcoming_apps,
                'services':serivces}
        return render(request,'home.html',data)


class RegisterAPIView(APIView):
    """
    API for registering a new user
    """
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')
    def post(self, request, *args, **kwargs):
        """_summary_
        Args:
        request (_type_): _description_
        """
        context = {}
        email = request.data.get('email')
        name =  request.data.get('first_name')
        l_name  = request.data.get('last_name')
        phone_number =  request.data.get('phone_number')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        username = request.data.get('username')
        print('--------------------1----------------------------')



        if not username:
            context['error']="Username is required"
            return render(request,'register.html',context)
        print('--------------------2----------------------------')

        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            context['error']="Username already exists"
            return render(request,'register.html',context)

        print('--------------------3----------------------------')
        if not is_valid_email(email):
            context['error']="Invalid email"
            return render(request,'register.html',context)

        print('--------------------4----------------------------')
        if isinstance(email,int):
            context['error']='Invalid email,expected a string'
            return render(request,'register.html',context)
        print('--------------------5----------------------------')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            context['error']="Email already exists"
            return render(request,'register.html',context)
        print('--------------------6----------------------------')
        if not is_valid_password(password):
            context['error']="Password is not valid ,must include 8 characters , uppercase , lowercase and number."
            return render(request,'register.html',context)
        print('--------------------7----------------------------')
        # if not check_password_for_spaces(password):
        #     context['error']="Password cannot contain spaces"
        #     return render(request,'register.html',context)
        print('--------------------8----------------------------')
        if not name:
            context['error']="Name cannot be empty"
            return render(request,'register.html',context)
        print('--------------------9----------------------------')
        if not phone_number:
            context['error']="Phone number cannot be empty"
            return render(request,'register.html',context)
        print('--------------------10----------------------------')
        if not confirm_password:
            context['error']="Confirm password cannot be empty."
            return render(request,'register.html',context)
        print('--------------------11----------------------------')
        if password != confirm_password:
            context['error']="Password and confirm password do not match"
            return render(request,'register.html',context)
        print('--------------------12----------------------------')
        request.session['email'] = email
        request.session.save()  # Ensure session data is saved
        request.session.modified = True  # Ensure that session changes are saved

        if not request.session.get('email'):
            context['error']='Error occured while storing email in session.'
            return render(request,'register.html',context)
        print('--------------------13----------------------------')
        otp = generate_otp()
        token = generate_random_string()
        verification_identifier = 'registration'
        print('--------------------14----------------------------')
        try:
            verification = VerificationToken.objects.create(name=verification_identifier,otp = otp,token = token)
        except Exception as e:
            context['error']=f"Error creating verification token: {str(e)}"
            return render(request,'register.html',context)
        print('--------------------15----------------------------')
        try:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=name,phone_number=phone_number,verification=verification,last_name=l_name)
            user.save()
            print('--------------------16----------------------------')
        except Exception as e:
            context['error']=f"Error creating user{str(e)}"
            return render(request,'register.html',context)
        print('--------------------17----------------------------')
        try:
            role = Role.objects.get(name='member')
        except Role.DoesNotExist:
            role = Role.objects.create(name='member')
            role.save()
        print('--------------------18----------------------------')
        member_data = {
                'user': user.id,
                'role': role.uuid,
            }
        member_instance = MemberCreateSerializers(data=member_data)
        if not member_instance.is_valid():
            verification.delete()
            user.delete()
            context['error']=f"Unable to create member {str(member_instance.errors)}"
            return render(request,'register.html',context)
        
        member_instance.save()
        member_instance = member_instance.data
        identifier='registration'

        member = get_member(user)

        data ={
            'email':email,
            'verification_code':otp,
            'token':token,
            'identifier':identifier,
            'uuid':member.uuid,
            'name':name


        }

        print("Session data:", request.session.items())

        
        email_verification_code = verify_user(identifier=identifier,data=data)
        if email_verification_code is False:
            print(f"------------------------")
            member.delete()
            verification.delete()
            user.delete()
            context['error']='Unable to send verification code'
            return render(request,'register.html',context)
        context['success']='User has created successfully and verification code has send your mail.'
        return render(request,'verify_otp.html',context)
        

class OTPVerifyAPIView(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """

    def get(self,request,*args,**kwargs):
        """_summary_
        """
        context={}
        print("Session data:", request.session.items())
        return render(request,'verify_otp.html',context)

    def post(self,request,*args,**kwargs):
        """_summary_
        """
        context={}
        print("Session data:", request.session.items())
        try:
            email = request.session.get('email')
        except Exception as e:
            context['error']=f"Unable to retrive mail from session : {str(e)}"
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            context['error']='Unable to find user with email.Go to register page and register  again.'
            return render(request,'verify_otp.html',context)

        input_otp = request.data.get('otp')
        if not  input_otp:
            context['error']='Please enter otp'
            return render(request,'verify_otp.html',context)

        try:
            member = get_member(user)
        except Exception as e:
            context['error']=f"Unable to get member : {str(e)}"
            return render(request,'verify_otp.html',context)
        
        
        otp =  user.verification.otp
        print(f"input = {otp}-----{input_otp}")
        print(f"input = {type(str(otp))}-----{type(input_otp)}")

        if str(otp) != str(input_otp):
            context['error']='Incorrect OTP'
            return render(request,'verify_otp.html',context)
        user.is_active = True
        member.is_active=True
        user.save()
        member.save()
        context['success']='Account activated successfully,please login to your account.'
        del request.session['email']
        return render(request,'login.html',context)
        
class VerifyMailLinkAPIView(APIView):
    """_summary_
    """
    def get(self,request,*args,**kwargs):
        """_summary_
        """
        context={}
        identifier_list = ['registration','invitation','verify']
        identifier = request.GET.get('identifier')
        verification =  request.GET.get('verification_token')
        uuid  = request.GET.get('uuid')
        print(f"verification ==  {verification}")

        try:
            email = request.session.get('email')
        except Exception as e:
            context['error']=f"Unable to retrive mail from session or user has been already verified and active : {str(e)}"

        try:
            user =  User.objects.get(email=email)
        except User.DoesNotExist:
            context['error']='Unable to find user with email.Go to register page and register  again or contact  us for help.'
            return render(request,'login.html',context)

        try:
            member = get_member(user)
        except Exception as e:
            context['error']='Unable to find member with user.'
            return render(request,'login.html',context)

        if not uuid:
            context['error']='UUID  is missing.'
            return render(request,'login.html',context)

        if not verification:
            context['error']='Verification code is  missing.'
            return render(request,'login.html',context)

        if not identifier:
            context['error']='Identifier is  missing.'
            return render(request,'login.html',context)

        if identifier not in identifier_list:
            context['error']='Invalid identifier,Contact us for help.'
            return render(request,'login.html',context)
    
    
        print(f"member uuid {type(uuid)}------------{type(member.uuid)}")
        print(f"member uuid {uuid}------------{member.uuid}")

        if str(uuid) != str(member.uuid):
            context['error']="UUID is does not match with member's uuid"
            return render(request,'login.html',context)

        if user.is_active is True and member.is_active is  True:
            context['error']='User is already active and verified,please login to your account.'

        if  verification != user.verification.token:
            context['error']='Verification code is not correct.'
            return render(request,'login.html',context)
        del request.session['email']
        user.is_active = True
        member.is_active=True
        user.save()
        member.save()
        verification = VerificationToken.objects.get(token = str(verification))
        verification.delete()
        
        context['success']='Your mail is verified successfully,please login to your account.'
        return render(request,'login.html',context)




class ResendVerificationAPIView(APIView):
    def get(self,request,*args,**kwargs):
        context={}
        context['mail']='required'
        return render(request,'verify_otp.html',context)
    def post(self,request):
        context={}
        email = request.POST.get('email')

        if not email:
            context['mail']='Required'
            context['error']='Email is missing.'
            return render(request,'verify_otp.html',context)    
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            context['error']='User does not exist with user and enter a correct mail id associated with user'
            context['mail']='Required'
            return render(request,'verify_otp.html',context)
        verification_identifier = 'resend_verification'
        otp = generate_otp()
        token = generate_random_string()

        try:
            verification = VerificationToken.objects.create(name=verification_identifier,otp = otp,token = token)
        except Exception as e:
            context['error']=f"Error creating verification token: {str(e)}"
            return render(request,'register.html',context)

        member = get_member(user)

        data ={
            'email':email,
            'verification_code':otp,
            'token':token,
            'identifier':verification_identifier,
            'uuid':member.uuid,
            'name':user.first_name


        }
        
        email_verification_code = verify_user(identifier=verification_identifier,data=data)
        if email_verification_code is False:
            context['error']='Failed to send verification code'
            return render(request,'verify_otp.html',context)
        context['success']="Verification send successfully to your email account."
        return render(request,'verify_otp.html',context)
          


