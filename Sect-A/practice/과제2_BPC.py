'''
##### 환율계산기(KRW/USD) #####
보낼 떄 송금 환율을 입력하세요 => 1,123.40
받을 떄 송금 환율을 입력하세요 => 1,102.60
---------------------------------------------------------------------------------------
[NOTICE]
 * 현재의 송금 환율은 보낼 때 1,123.40, 받을 떄 1,102.60입니다.
 * 송금환율 리스트 [보낼때, 받을때] :  [1123.4, 1102.6]
---------------------------------------------------------------------------------------
미국에서 송금할 미화(USD) 금액을 입력하세요 => 1000
한국에서 송금할 한화(KRW) 금액을 입력하세요 => 1124400
---------------------------------------------------------------------------------------
[RESULT]
 * 받을 떄 : 1000.00 USD => 1102600 KRW
 * 보낼 떄 : 1124400 KRW => 1000.00 USD

rate_send
rate_recv
rate_list

m1_usd_send
m1_krw_recv
m2_usd_send
m2_krw_recv

'''

print('##### 환율계산기(KRW/USD) #####')
rate_send = input("보낼 떄 송금 환율을 입력하세요 => ")
rate_recv = input("받을 떄 송금 환율을 입력하세요 => ")

rate_list = []

rate_send = rate_send.replace(' ', '')
rate_send = rate_send.replace(',', '')
rate_send = float(rate_send)

rate_recv = rate_recv.replace(' ', '')
rate_recv = rate_recv.replace(',', '')
rate_recv = float(rate_recv)

rate_list.append(rate_send)
rate_list.append(rate_recv)

print('-'*80)
print(' * 현재의 송금 환율은 보낼 때 {}, 받을 떄 {}입니다.'.format(rate_send, rate_recv))
print(' * 송금환율 리스트 [보낼때, 받을때] :  {}'.format(rate_list))

print('-'*80)

m1_usd_send = input('미국에서 송금할 미화(USD) 금액을 입력하세요 => ')
m2_krw_recv = input('한국에서 송금할 한화(KRW) 금액을 입력하세요 => ')

m1_usd_send = float(m1_usd_send)
m2_krw_recv = float(m2_krw_recv)

# m1_krw_send = m1_usd_send * rate_recv
# m2_usd_send = m2_krw_recv / rate_send

m1_krw_send = m1_usd_send * rate_list[0]
m2_usd_send = m2_krw_recv / rate_list[1]

print('-'*80)
print('[RESULT]')
print('* 받을 떄 : %.2f USD => %d KRW'%(m1_usd_send, int(m1_krw_send)))
print('* 보낼 떄 : %d KRW => %.2f USD'%(int(m2_krw_recv), m2_usd_send))


