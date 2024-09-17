from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactMessageSerializer
from django.core.mail import EmailMessage
from django.conf import settings
class ContactMessageCreateView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            
            # Debugging output
           
            print(f'Subject: {subject}')
            print(f'Message: {message}')
            
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=serializer.validated_data['email'],
                
                to=[settings.EMAIL_HOST_USER]
                        
            )
            
            email.send()
            
            return Response({'status': 'Message sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
