from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Question, Answer
from django.http import HttpResponseNotAllowed
from ..forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q 
# or 조건으로 조회할 수 있는 Q

def index(request):
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw','') #검색어
    question_list = Question.objects.order_by('-create_date') #게시물 전체 의미
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목 검색(제목에 kw문자열이 포함되었는지 확인)
            Q(content__icontains=kw) | #내용 검색
            Q(answer__content__icontains=kw) | #답변 내용 검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()
        # distinct 메소드는 중복된 항목은 제외하고 출력해줌
        # filter 함수에서 모델 속성에 접근하기 위해서는 이처럼 __ (언더바 두개) 를 이용하여 하위 속성에 접근할 수 있음
        # ※ subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw} #question_list는 페이징 객체(page_pbj)
    # context = {'question_list': question_list} #기존에 있던 항목으로 입력된 내용 전체를 불러와서 위와 같이 페이지 수 제한함
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
