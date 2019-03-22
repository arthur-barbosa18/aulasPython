import requests
i = 0
while(True):
  print(i)
  i = i+1
  url = "https://www.submarino.com.br/produto/133731106"

  querystring = {"DCSext.recom":"RR_home_page.rr1-PopularProducts","nm_origem":"rec_home_page.rr1-PopularProducts","nm_ranking_rec":"2","pfm_carac":"S%C3%B3%20as%20melhores%20ofertas","pfm_index":"1","pfm_page":"home","pfm_pos":"home_page.rr1","pfm_type":"vit_recommendation"}

  payload = ""
  headers = {
      'cache-control': "no-cache",
      'Postman-Token': "0048c699-cb22-48cd-8d05-06b9aa14027e"
      }

  response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

  #print(response.text)
  #print(response.text.index('class="buybox__Value-sc-12kaghb-2 hokx TextUI-sc-1hrwx40-0 eMlBOZ">'))

  #print(response.text)
  #for i in response.texxt:
  #  if()

  #if('class="buybox__Value-sc-12kaghb-2 hokx TextUI-sc-1hrwx40-0 eMlBOZ">' in  )
  #HomeSubmarino = open('HomeSubmarino.html', 'w')
  #HomeSubmarino.write(response.text)
  print(response.text[response.text.index(\
    'class="buybox__Value-sc-12kaghb-2 hokx TextUI-sc-1hrwx40-0 eMlBOZ">')+67\
    :response.text.index('class="buybox__Value-sc-12kaghb-2 hokx TextUI-sc-1hrwx40-0 eMlBOZ">')+11+64])
  #class="buybox__Value-sc-12kaghb-2 hokx TextUI-sc-1hrwx40-0 eMlBOZ">
  #11