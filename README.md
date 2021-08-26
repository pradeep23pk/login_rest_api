# login_rest_api

Features:

Available api
1) for signup http://127.0.0.1:8000/register/
2) view users list http://127.0.0.1:8000/users/
3) view transaction history with masked email of users http://127.0.0.1:8000/history/
4) view how many users use his code to signup and earned incentives http://127.0.0.1:8000/referalspec/AzQJtxDR
5) view list of all users who referred http://127.0.0.1:8000/referal/

-> User can signup with referral-code and earn point at "http://127.0.0.1:8000/register/" if code is correct
{
    "name" : "pradeep",
    "email":"abcd@gmail.com",
    "passwords":"okdear",
    "referred":"ZPwrIBbt"    #valid referal code of user name "a2"
}
-> user can see transaction history of users which contain masked email and their respective inscentives at "http://127.0.0.1:8000/history/" 
-> user can see, how many users has used his code to signup, and earned incentives ,at "http://127.0.0.1:8000/referalspec/AzQJtxDR"  #where (AzQJtxDR) is referal code of user Ranaappa

an user earn through referring other user
