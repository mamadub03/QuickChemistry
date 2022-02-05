from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from quickapp.models import ChemProblems
from django_compounds import gen
# Create your views here.


def index(request):
    return render(request,'qwik/index.html')

def generator(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("TYPE: " + form.cleaned_data['bond'])
            print("AMOUNT:" + str(form.cleaned_data['amount']))


            run = True
            for i in range(form.cleaned_data['amount']):

                if ChemProblems.objects.exists() and run == True:
                    prob= ChemProblems.objects.all()
                    for i in prob:
                        i.delete()
                        print("DELETED")

                run = False
                x = gen(form.cleaned_data['amount'],form.cleaned_data['bond'])
                user = ChemProblems.objects.get_or_create(problem=x)
                print("CREATED NEW ONES!")
            print('COMPLETE!')

    print(form.is_bound)
    return render(request,'qwik/generator.html',{'form':form})

def problems(request):
    problem_list = ChemProblems.objects.order_by("problem")
    problem_dict = {'problems':problem_list}
    for e in problem_list:
        print(e)

    if ChemProblems.objects.order_by("problem").exists():
        print("EXIST")
        return render(request,'qwik/problems.html',context=problem_dict)
