# coding=gbk
from sys import * 
from ctypes import * 
import json
#������ص���64λ��DLL   ����32��Ҳһ��������    
Dll = WinDLL("t_json")#����DLL

#���彻�׽ӿں����������͡�������������������������������������������������������������������������������������������������������������������������������������������������������������������
    #������Ҳ��������������д�ˣ�
#���庯���������͡�������������������������������������������������������������������������������������������������������������������
Dll.Logon.restype =  POINTER(c_void_p)
#Dll.Logoff.restype =  c_void
Dll.QueryData.restype = c_int 
Dll.SendOrder.restype = c_int 
Dll.QueryHQ.restype = c_int 
Dll.CancelOrder.restype = c_int 
Dll.CancelOrder.CancelOrder = c_int 
Dll.QueryHistoryData.restype = c_int 




print("���׽ӿڲ��ԡ�������������������������������������������������")
qsid = 0
host = c_buffer(b"trade.10jqka.com.cn")#ʵ������ϵ��Ȩ panghu1103@gmail.com
post  = 8002
version = c_buffer(b"E065.18.81.002")
yybid = c_buffer(b"")#Ӫҵ��ID  ����ȯ�̲���Ҫ������� ����Ҫѡ��Ӫҵ������� ��Ҫ�������
accounttype = 0x30
account = c_buffer(b"xxx")#�Լ����ʽ��˺�
password = c_buffer(b"xxxx")#д�Լ�Ҫ����
comm_password = c_buffer(b"")#ͨѶ����û�о�����
#����������������������������������������������������������������������������������������������Ҫ����������������������������������������������������������������������������
Out = c_buffer(1024*1024)#���߳���Ҫд�ɾֲ����������ڴ��ͻ��ɱ���

print("��¼���׽ӿ�=====================================================")
ClientID = Dll.Logon(qsid, host, post, version, yybid, accounttype,account,password,comm_password,False,Out)

if ClientID:
    print("��¼�ɹ����ͻ���ID",ClientID)
else:
    print(Out.value.decode('gb2312'))
    exit()
print("��ѯ�ʲ�=====================================================")
Category = 0 #��ѯ��Ϣ������ 0�ʽ� 1�ɷ� 2����ί�� 3���ճɽ� 4����ί�пɳ��� 5�ɶ��˻� 12=���깺�¹� 13=�깺��� 14=��Ų�ѯ 15=��ǩ��ѯ
b = Dll.QueryData(ClientID,Category,Out)
if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))
    print(_json)
else:
    print(Out.value.decode('gb2312'))

print("�嵵����=====================================================")

Zqdm = c_buffer(b"000001")
b = Dll.QueryHQ(ClientID,Zqdm,Out)

if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))

print("�ֲֹ�Ʊ=====================================================")
Category = 1
b = Dll.QueryData(ClientID,Category,Out)

if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))
print("�µ�=====================================================")

Category = 0    #0�� 1��
Gddm = c_buffer(b"")    #�ɶ����� �ɿ� ָ���ɶ��˻����������ָ���ɶ�
Zqdm = c_buffer(b"000001")
Price = c_float(8.99)
Quantity = 100

b = Dll.SendOrder(ClientID, Category, Gddm, Zqdm, Price, Quantity, Out)
if b > 0 :
    OrderID = Out.value.decode('gb2312')

    print("�µ��ɹ�����ͬ��ţ�",OrderID)

    print("����=====================================================")

    OrderID = OrderID.encode('utf-8')

    b = Dll.CancelOrder(ClientID, OrderID, Out)

    if b > 0 :

        OrderID = Out.value.decode('gb2312')

        print("�����ɹ�,��ͬ��ţ�",OrderID)
    else:
        print(Out.value.decode('gb2312'))

else:
    print(Out.value.decode('gb2312'))


#���׽ӿ���������ʹ�ø������࣬�Ͳ�һһ��ʾ�ˡ���������������������������������������������������������������������������������������������������������������


#���濴����ӿ���ʾ��������������������������������������������������������������������������������������������������������������������������������������������������������������������
#��������ӿں����������͡�������������������������������������������������������������������������������������������������������������������������������������������������������������������
Dll.HQ_Logon.restype =  POINTER(c_void_p)
#Dll.HQ_Logoff.restype =  c_void
Dll.HQ_QueryData.restype =  c_int
Dll.HQ_PushData.restype =  c_int


print("����ӿڲ��ԡ�����������������������������������������������")

Host = c_buffer(b"112.17.10.222")#���������IP
Port = 9601#�˿�
account = c_buffer(b"xxx")#�Լ���LS�ֻ��� ��ͨ�˺��޷���ѯ��L2����
password = c_buffer(b"xxx")#д�Լ�Ҫ����
print("�����¼����������������������������������������������������")
ClientID = Dll.HQ_Logon (Host, Port, account, password, Out)
if ClientID:
    print("�����¼�ɹ����ͻ���ID",ClientID)
else:
    print(Out.value.decode('gb2312'))
    exit()

print("ʮ��������ԡ�����������������������������������������������")
#�Զ���Ҫ��ѯ���ֶ� �൱�ڲ�ѯ���ݿ��ֶε���˼
#��Ʊ���� ����һ�β�ѯ��ֻ��Ʊ������   ���Ǳ�����ͬһ������  ���� ��һֻ��Ʊ�����ڰ��� ��ô�ڶ�ֻҲҪ�����ڰ��ɲ���һ�δﵽ������ѯ
#custom_data��Ҫ��ѯ���ֶ�  �����Զ������ӻ�����������Լ���Ҫ��ѯ������
custom_data = c_buffer(b"id=200&market=USZA&codelist=000001&datatype=5,6,7,10,13,24,25,26,27,28,29,30,31,32,33,34,35,69,70,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,150,151,152,153,154,155,156,157,1968584,201,202,203,204,205,206,207,208,209,210,211,212,213,214,3541450,3475914")#����
b = Dll.HQ_QueryData(ClientID,custom_data,Out)
if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))
print("�ɽ���ϸ���ԡ�����������������������������������������������")

custom_data = c_buffer(b"id=220&market=USZA&code=000001&start=-32&end=0&datatype=10,12,13")

b = Dll.HQ_QueryData(ClientID,custom_data,Out)
if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))

print("�����жӲ��ԡ�����������������������������������������������")

custom_data = c_buffer(b"id=223&market=USZA&code=000001&codelist=000001&datatype=10")

b = Dll.HQ_QueryData(ClientID,custom_data,Out)
if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))

print("�����Ƿ�����������������������������������������������������")
#&sortcount=7��ȡ7ֻ����&sortid=527527��1��������ID��527526��3���ӣ�3934664��5���ӣ�461438��10���ӣ�461439��15���ӣ�
custom_data = c_buffer(b"id=7&blockid=E&reqflag=blockserver&sortbegin=0&sortcount=7&sortid=527527&sortorder=D")

b = Dll.HQ_QueryData(ClientID,custom_data,Out)
if b > 0 :
    _json = json.loads(Out.value.decode('gb2312'))

    print(_json)
else:
    print(Out.value.decode('gb2312'))



#ֻ�ڿ����ڼ�Ż����������͹���
#���»ص�����  ÿ�����ܶ����Զ��岻ͬ�Ļص�
#-------------------------------------------------------------------һ�¹���ֻ�ڿ����ڼ���Ч  ����û�в��� ��֪����û��д��

print('�������Ͳ���=====================================================')
���ͻص����� = CFUNCTYPE(c_int, POINTER(c_char_p))
def ���ͻص�����(type, Result):
    if type == 10001:#��ͨʮ������ 3��
        _json = json.loads(Out.value.decode('gb2312'))

        print(_json)
    elif type == 10206:# ���ί��
        _json = json.loads(Out.value.decode('gb2312'))

        print(_json)
    elif type == 10207:#ȫ��500��ת10��
        _json = json.loads(Out.value.decode('gb2312'))

        print(_json)
���ͻص�����ָ�� = ���ͻص�����(���ͻص�����)
Zqdm = c_buffer(b"000001")
b = Dll.HQ_PushData(ID, 0, Zqdm, ���ͻص�����ָ��, True);#����2 0Ϊʮ���������ͼ��3�� 1Ϊ���ί�к��뼶ȫ�� 2Ϊȫ��10�� ����6 ��Ϊ������ֻ��Ʊ����  ��Ϊ�ر���ֻ������
if b > 0 :
    print('�����ɹ�����ʾ')
else:
    print(Out.value.decode('gb2312'))

