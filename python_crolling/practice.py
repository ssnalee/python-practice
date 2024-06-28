import requests
url = 'http://nadocoding.tistory.com'
headers ={"User-Agent" : "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
# res = requests.get('http://naver.com')
res = requests.get(url, headers=headers)

# if res.status_code == requests.codes.ok :
#     print("정상입니다")
# else :
#     print("문제가 생겼다.",res.status_code)
    
res.raise_for_status()
print(len(res.text))

with open('nadocoding.html','w',encoding='utf-8') as f :
    f.write(res.text)

# import re
# abck, book, desk      # $ : 문자열의 끝         re.compile('k$')   
# care cafe case cave   # ^ : 문자열의 시작       re.compile('^c')
# caae cabe cace cade   # . : 하나의 문자를 의미  re.compile('ca.e')      
# p = re.compile('ca.e')       

# def print_match(m) :
#     # print(m.group()) #매치되지 않으면 error 발생

#     if m :
#        print('m.group()',m.group())  #일치하는 문자열 반환
#        print('m.string',m.string)    #입력받은 문자열
#        print('m.start()',m.start())  #일치하는 문자열의 시작 index
#        print('m.end()',m.end())      #일치하는 문자열의 끝 index
#        print('m.span()',m.span())    #일치하는 문자열의 시작 / 끝 index
#     else : 
#         print('매칭안댐')

# # m = p.match("assa") # match : 주어진 문자열의 처음부터 일치하는지 확인
# # print_match(m)

# # m = p.search('good care') #search : 주어진 문자열 중에 일치하는게 있는지 확인
# # print_match(m)

# lst = p.findall('good care cafe')
# print(lst)

#1. p = re.compile('원하는 형태')
#2. m = p.match('비교할 문자열) : 주어진 문자열의 처음부터 일치하는지 확인
#3. m = p.search('비교할 문자열) : 일치하는 모든 것을 '리스트'형태로 보관가능