import streamlit as st
import requests

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()
	return res

def getCountyOption(items,target):
	optionList=[]
	for item in items:
		name = item['cityName'][0:3]
		if name not in optionList: 
			optionList.append(name)
	return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
		name = item['cityName']
		if county in name: 
			specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(items):
	expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])
        expander.subheader('Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['openTime'])
		expander.subheader('Email')
		expander.write(item['email'])
		expanderList.append(expender)
    return expanderList

def app():
	bookstorelist = getAllBookstore
	countyOption = getCountyOption(bookstoreList)
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstorelist))
	county = st.selectbox('請選擇縣市', countyOption)
	districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域',districtOption)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)

if __name__ == '__main__':
    app()

