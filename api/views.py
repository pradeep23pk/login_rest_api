from .models import RefCode, user,history
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userSerializer,historySerializer,RefCodeSerializer

def mask(email):
    return (email[0]+"******"+email[-5:])

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    print(serializer)
    ref_code = request.data['referred']
    credit = False
    if ref_code:
        print(ref_code)
        check_code = user.objects.filter(referral_code=str(ref_code))
        if check_code:
            get_user = user.objects.get(referral_code=str(ref_code))
            transaction = RefCode.objects.create(code=ref_code,from_name=get_user.name,to_name=request.data['name'])
            History=history.objects.create(usingCode=ref_code,userEmail=request.data['email'],referalEmail=get_user.email)
            History.save()
            transaction.save() 
            get_user.incentives += 100
            get_user.save() 
            credit = True
        else:
            return Response("Invalid ref code")
    else:
        return Response("invalid referral code")
    serializer.is_valid(raise_exception=True)
    serializer.save()
    if credit:
        get_log_user = user.objects.get(id = serializer.data['id'])
        get_log_user.incentives+= 100
        get_log_user.save()
        txn=history.objects.get(userEmail=request.data['email'])
        txn.userIncentive +=100
        txn.referalIncentive +=100
        txn.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_userlist(request):
    users=user.objects.all()
    serializer=userSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_referallist(request):
    users=RefCode.objects.all()
    serializer=RefCodeSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_spcificCode(request,pk):
    users=RefCode.objects.filter(code=pk)
    serializer=RefCodeSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_referallist(request,):
    users=RefCode.objects.all()
    serializer=RefCodeSerializer(users,many=True)
    print("\n serialized data:", serializer)
    return Response(serializer.data)


@api_view(['GET'])
def get_history(request):
    history_list= history.objects.all()
    serializer=historySerializer(history_list,many=True)
    for data in serializer.data:
        data['userEmail']=mask(data['userEmail'])
        data['referalEmail']=mask(data['referalEmail'])
        
    return Response(serializer.data)










