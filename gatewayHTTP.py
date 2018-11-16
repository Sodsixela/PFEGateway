import requets
import json

headers = {'content-type' : 'application/json'}
data = {"giletid":"0123456789",
		"global":[{
					"date":"2018-11-16",
					"data":[{
								"typeId":"000",
								"sensor":{
											"x1":"18",
											"y1":"20",
											"z1":"23",
											"x2":"9",
											"y2":"14",
											"z2":"51"
										}
							}]
				}]
		}
requests.post(url, json=data)
											
										