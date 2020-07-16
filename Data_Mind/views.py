from django.http import HttpResponse
from django.shortcuts import render
import json
from pyspark import SparkContext, SparkConf, HiveContext
# Create your views here.
from Data_Mind.DataBase import savebook, findallbook


def index(request):
    para = request.POST["requestParam"]
    contex = {}
    contex['user_name'] = para
    return render(request,'index.html',contex)


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def nopass(request):
    return render(request,'nopassword.html')


def auth(request):
    back_dic = {"username": 0, 'password': 0}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username =='root' or username=='user':
            back_dic['username'] = username
            back_dic['password'] = password
    return HttpResponse(json.dumps(back_dic))


def testserlet(request):
    ret =findallbook()
    return HttpResponse(json.dumps(ret))

def test_spark(request):
    # conf = SparkConf().setMaster('local').setAppName('SparkTest')
    # sc = SparkContext(conf=conf)  # 连接到spark集群
    # text3 = sc.textFile("hdfs://127.0.0.1:9000/New/wordcount.txt")
    # wordCount = text3.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    # wordCount.foreach(print)

    conf = SparkConf().setMaster("local").setAppName("My App")
    sc = SparkContext(conf=conf)
    hive_context = HiveContext(sc)

    # 生成查询的SQL语句，这个跟hive的查询语句一样，所以也可以加where等条件语句
    # hive_database = "default"
    # hive_table = "xp"
    hive_read = "select * from  default.student"#.format(hive_database, hive_table)

    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    hive_context.sql("show databases").show(100)
    hive_context.sql("use default")
    hive_context.sql("show tables").show(100)
    a=hive_context.sql("select * from student").collect()[0]
    print(a['name'])
    sc.stop()
    return HttpResponse(a)