from django.http import JsonResponse
from django.shortcuts import redirect
from crudapp.models import Student
from crudapp.forms import StudentForm
import json
from django.views.decorators.csrf import csrf_exempt
from .models import StudentMarks, Marklist
from operator import itemgetter 
import pprint


def retrieve(request):
	student=Student.objects.all()
	
	a=list((student.values()))
	print("the length of a is: ",len(a))

	#print("the list s",)
	# student list(Student.objects.values())
	return JsonResponse(a,safe = False)

	
	#return render(request, 'crudapp/index.html',context={'student':student})
@csrf_exempt
def AddDetail(request):
	try:
		#print("request.POst:",request.POST)
		data = json.loads(request.body.decode())

		#data=dict(request.POST.body)
		print(type(data))
		print("the data is: ",data)
		entry=Student.objects.create(
			serialno=data["serialno"], 
			firstname=data["firstname"],
			lastname=data["lastname"],
			gender=data["gender"],
			department=data["department"],
			phonenumber=data["phonenumber"],
			emailId=data["emailId"]
			)
		print("the entry data is: ",entry)
		

		# form=StudentForm()
		# if request.method=='POST':
		# 	form=StudentForm(request.POST)

		# 	if form.is_valid():
		# 		print("form",form)
		# 		form.save()
		# 		#form=request.form.to_dict()
		# 		print("after adding",form)
		# 	else:
		# 		raise Exception("form value data is :",form.is_valid())
	except Exception as e:
		print("error is: ",e)
		#return render(request, 'crudapp/create.html', context={'form':form})
		return JsonResponse("data not Added", safe=False)

	else:
		return redirect('/list')
		return JsonResponse("data Added", safe=False)


def deleteview(request,id):
	print("delete function",id)

	student=Student.objects.filter(id=id).exists()
	if not student:
		return JsonResponse("the data is not exists", safe=False)
	else:
		st=Student.objects.get(id=id)
		st.delete()
		return redirect('/list')
		return JsonResponse("data deleted", safe=False)

@csrf_exempt
def updateview(request,id):
	try:
		data = json.loads(request.body.decode())
		print("the data is: ",data)

		update=Student.objects.filter(id=id).update(serialno=data["serialno"], 
			firstname=data["firstname"],
			lastname=data["lastname"],
			gender=data["gender"],
			department=data["department"],
			phonenumber=data["phonenumber"],
			emailId=data["emailId"],
			)
		print("the update is:",update)

		# result=json.dumps(data)
		# print("the output is: ",result)
		
		# student=Student.objects.get(id=id)
		# context={}
		# if request.method=='POST':
		# 	form=StudentForm(request.POST,instance=student)
		# 	if form.is_valid():
		# 		form.save()
			# else:
			# 	raise Exception("form value data is :",form.is_valid())
	except Exception as ee:
		print("the error is:",ee)
		#return render(request, 'crudapp/update.html', {'student':student})
	else:
		return redirect('/list')
		return JsonResponse("data updated", safe=False)

@csrf_exempt
def Add_Marklist(request):
	try:
		my_list=json.loads(request.body.decode())
		a=Student.objects.get(id=my_list["StId"])
		if Marklist.objects.filter(StId=my_list["StId"]).exists():
			return JsonResponse("this student Id is already exists",safe=False)
		else:
			print("my_list[stid] is : ", a)
			data=Marklist.objects.create(
				StId=a,
				Language=my_list["Language"],
				Maths=my_list["Maths"],
				Physics=my_list["Physics"],
				Chemistry=my_list["Chemistry"],
				Biology=my_list["Biology"]
				)

		# my_records=list(Marklist.objects.filter(StId_id=my_list["StId"]).values())
		# print("my records is:",my_records)
		# for i in my_records:
		#     total=my_records[0]["Language"]+my_records[0]["Maths"]+my_records[0]["Physics"]+my_records[0]["Chemistry"]+my_records[0]["Biology"]
		#     print("the value of total:",total)
		#     i["Total"]=total
		#     print("the final data is:", my_records)


		#joining three table models...
			my_table=Student.objects.select_related("Marklist")
			my_data=(Marklist.objects.all())
			print("the type of my_data:",type(my_data))
			print("the lengthof my_data:",len(my_data))

			my_records=list(my_data.values())
			print("my records is:",my_records)
			for i in my_records:
				print("the value i is",i)
				total=i["Language"]+i["Maths"]+i["Physics"]+i["Chemistry"]+i["Biology"]
				print("the value of total:",total)
				i["Total"]=total
				print("the final data is:", my_records)

			#return redirect("/alltable")   
			return JsonResponse({'status':1,'data':"Data Added"}, safe=False)
	except Exception as e:
		print("the exception is :", e)
		return JsonResponse({'status':0,'data':str(e)},safe=False)   

    #return HTTPResponse(marks)
    #return JsonResponse(marks,safe=False)


def all_table(request):
    # a=Student.objects.all()
    # print("Student.object.all is :",a)
    # a_val=list(a.values())
    # print("the values of a is:",a_val)
    try:
        my_table=Marklist.objects.select_related("StId")
        print("the join table is : ", my_table)
       # my_marklist=Marklist.objects.all()
        marklist_val=list(my_table.values('StId_id','StId_id__serialno', 'StId_id__firstname',
            'StId_id__lastname', 'StId_id__gender', 'StId_id__department', 'StId_id__phonenumber',
            'StId_id__emailId','Language','Maths','Physics','Chemistry', 'Biology'))
        #print("the values of marklist_val is: ", marklist_val)

        for i in marklist_val:
            #print("the value i is",i)
            total=i["Language"]+i["Maths"]+i["Physics"]+i["Chemistry"]+i["Biology"]
            #print("the value of total:",total)
            i["Total"]=total
            #print("the final data is:", marklist_val)
        print("the length of all table is: ",len(marklist_val))
        
        #a=json.dumps(marklist_val)         #NO NEED OF CONVERSION INTO DICTIONARY WHEN WE RESPONDED INTO JSON...
        #print("the table view of a is: ", a)
        return JsonResponse({'status':1,'data':marklist_val}, safe=False)
       
    except Exception as e:
        print("the exception in alltable is:",e)

        return JsonResponse({'status':0,'data':e}, safe=False)

@csrf_exempt
def Stu_Marklist(request):
    try:
        #x=request.objects.all()
        #print("the request.obj is:", request.GET)
        
        #print("the value of x is: ",x)
        my_table=Marklist.objects.select_related("StId")
        print("the my_table is: ",my_table)
        print("the my_table type is: ", type(my_table))
        #m=my_table.values()
        #print("the values of m;", m)
        my_id = request.GET.get('StId')
        marklist_val=list(my_table.filter(StId=my_id).values('StId_id__id', 'StId_id__serialno', 'StId_id__firstname',
            'StId_id__lastname', 'StId_id__gender', 'StId_id__department', 'StId_id__phonenumber',
            'StId_id__emailId','Language','Maths','Physics','Chemistry', 'Biology'))
        #print("the values of marklist_val is: ", marklist_val)

        for i in marklist_val:
            #print("the value i is", i)
            total=i["Language"]+i["Maths"]+i["Physics"]+i["Chemistry"]+i["Biology"]
            #print("the value of total:",total)
            i["Total"]=total

            print("the final data is:", marklist_val)
        # student_array=[]
        # print("the type of array is:",type(student_array))
        # my_id = request.GET.get('StId')
        # print("the value of StIdis", my_id)
        # Studentdetails=Marklist.objects.filter(StId=StId_id).values()
        # #Studentdetails= Marklist.objects.filter(StId = StId_id)
        # print("the student details is:", Studentdetails)
        # student_array.append(Studentdetails)
        # #print("the arraytype is:",type(student_array))
        #x=json.dumps(student_array)


        return JsonResponse({'status':1,'data':marklist_val}, safe=False)
        #return JsonResponse("marklist",safe=False)
    except Exception as e:
        print("the Exception is: ",e)
        return JsonResponse({'status':0,'data':e}, safe=False)

def Sub_wise_marks(request):
    try:
        my_table=Marklist.objects.select_related("StId")
        print("my_table is: ",my_table)
        my_id = request.GET.get('StId')
        print("the My_id is: ", my_id)
        marklist_val=list(my_table.filter(StId=my_id).values('Language','Maths','Physics','Chemistry', 'Biology'))
        print("the values of marklist_val is: ", marklist_val)
        my_dict=marklist_val[0]
        print("the value of my_dict is:",my_dict)

        sort_orders = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        x=dict(sort_orders)

        print("the sorted order is : ", x)

        # sort_orders =list(sorted(marklist_val.items(), key=lambda x: x[1], reverse=True))

        # for i in sort_orders:
        #     print(i[0], i[1])

        # x=list.sorted(marklist_val.items(), key = lambda x: x[1], reverse = True)
        # my_list = []
        # for i in marklist_val:
        #     my_list.append(i)

        #print("the sorted llist",x)
        # for i in sort_orders:
        #     #print("the value i is",i)
        #     total=i["Language"]+i["Maths"]+i["Physics"]+i["Chemistry"]+i["Biology"]
        #     #print("the value of total:",total)
        #     i["Total"]=total
        #     #print("the final data is:", marklist_val)
                
        #print("the value of Desorder s:", Desorder)
        return JsonResponse({'status':1,'data':x},safe=False)
    except Exception as e:
        print("The Exception is: ",e)
        return JsonResponse({'status':0,'data':e}, safe=False)

def high_lower_submark(request):
    try:
        # my_id = request.GET.get('name')
        # print("the name is:",name)

        my_table=Marklist.objects.select_related("StId")

        marklist_val=list(my_table.values('StId_id','StId_id__serialno', 'StId_id__firstname',
            'StId_id__lastname', 'Language','Maths','Physics','Chemistry', 'Biology'))
        #print("the values of marklist_val is: ", marklist_val)

        # Physics=sorted(marklist_val, key=itemgetter('Physics'), reverse=True)
        # print("Physics marks are: ",Physics)
        # highscore = max(marklist_val, key=lambda x:x['Physics'])
        # print("highscore in physics : ", highscore)
        # lowscore = min(marklist_val, key=lambda x:x['Physics'])
        # print("lowscore in physics is : ",lowscore)


        subid=request.GET.get('name')
        print("the request.GET.get is", request.GET.get('name'))
        if subid=='Chemistry':
            print("the language is:",subid)
            x=sorted(marklist_val, key=itemgetter('Chemistry'), reverse=True)
            highscore = max(marklist_val, key=lambda x:x['Chemistry'])
            lowscore = min(marklist_val, key=lambda x:x['Chemistry'])
            a={"highscorer": highscore,"lowerscorer": lowscore}
        elif subid=='Language':
            print("the language is:",subid)
            x=sorted(marklist_val, key=itemgetter('Language'), reverse=True)
            highscore = max(marklist_val, key=lambda x:x['Language'])
            lowscore = min(marklist_val, key=lambda x:x['Language'])
            a={"highscorer": highscore,"lowerscorer": lowscore}
        elif subid=='Maths':
            print("the language is:",subid)
            x=sorted(marklist_val, key=itemgetter('Maths'), reverse=True)
            highscore = max(marklist_val, key=lambda x:x['Maths'])
            lowscore = min(marklist_val, key=lambda x:x['Maths'])
            a={"highscorer": highscore,"lowerscorer": lowscore}
        elif subid=='Physics':
            print("the language is:",subid)
            x=sorted(marklist_val, key=itemgetter('Physics'), reverse=True)
            highscore = max(marklist_val, key=lambda x:x['Physics'])
            lowscore = min(marklist_val, key=lambda x:x['Physics'])
            a={"highscorer": highscore,"lowerscorer": lowscore}
        elif subid=='Biology':
            print("the language is:",subid)
            x=sorted(marklist_val, key=itemgetter('Biology'), reverse=True)
            highscore = max(marklist_val, key=lambda x:x['Biology'])
            lowscore = min(marklist_val, key=lambda x:x['Biology'])
            a={"highscorer": highscore,"lowerscorer": lowscore}
        else:
            a="The requested Subject Name is not exists"
        return JsonResponse({'status':1,'data':a}, safe=False)
    except Exception as e:
        print("The Exception is : ",e)
        return JsonResponse({'status':0,'data':e},safe=False)

def deletemark(request,id):
	s = Marklist.objects.filter(StId=int(id)).delete()
	
	print("what is s:",s)
	#s.delete()
	return JsonResponse("data deleted", safe=False)
		