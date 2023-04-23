def index_view(request):
    return render(request,'index.html')


def bf_view(request):
    form=bf_form()
    return render(request,"bf.html",{'form':form,})

def gf_view(request):
    bf_name=request.GET['bname']
    form=gf_form()
    request.session['bname']=bf_name
    return render(request,"gf.html",{'form':form,'bf_name':bf_name})


def age_view(request):
    bf_name=request.session.get('bname')
    gf_name=request.GET['gname']
    form=age_form()
    request.session['gname']=gf_name
    return render(request,"age.html",{'form':form,'bf_name':bf_name})


def result_view(request):
    bf_name=request.session.get('bname')
    gf_name=request.session.get('gname')
    bage=request.GET['age']
    request.session['age']=bage
    return render(request,"result.html",{'bf_name':bf_name,'gf_name':gf_name,'bage':bage})

