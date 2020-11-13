import mysql.connector
import random
try:
	database = mysql.connector.connect(
		host="remotemysql.com",
	  	user="4qYqvMgCab",
	  	password="1NtT5Pl65o",
	  	database="4qYqvMgCab"
	)
	cursor = database.cursor()
	def main():
		select = int(input("1-GİRİŞ YAP\n2-KAYIT OL\n"))
		if select == 1:
			login()
		elif select == 2:
			register()
		else:
			forloop()
	def forloop():
		print("Yanlış Seçim")
		main()
	def login():
		username = input("Kullanıcı Adını Giriniz : ")
		password = input("Şifrenizi Giriniz : ")
		data = (username,)
		sqlcheck = "SELECT * FROM uyeler WHERE username = %s"
		cursor.execute(sqlcheck,data)
		result = cursor.fetchall()
		if result == []:
			print("Kullanıcı adı veya şifre yanlış")
		else:
			for i in result:
				if username in i and password in i:
					print("Giriş Başarılı")
				else:
					print("Kullanıcı adı veya şifre yanlış")

	def register():
		username = input("Kullanıcı Adını Giriniz : ")	
		password = input("Şifrenizi Giriniz : ")
		data = (username,)
		sqlcheck = "SELECT * FROM uyeler WHERE username = %s"
		cursor.execute(sqlcheck,data)
		result = cursor.fetchall()
		if result == []:
			adduser(username,password)
		else:
			for i in result:
				print("Böyle Kullanıcı Mevcut")
				register()
	def adduser(username,password):
		try:
			sql = "INSERT INTO uyeler (username,password) VALUES (%s,%s)"
			value = (username,password)
			cursor.execute(sql,value)
			database.commit()
			print("Kullanıcı Eklendi.")
		except:	
			print("Hata")

except:
	print("Sunucuya Bağlanılamadı")
main()
