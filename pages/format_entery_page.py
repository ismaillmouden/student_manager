from flet import *
import sqlite3
###############################----- feilds ------#######################

tname = TextField(label="اسم الطالب",rtl=True,height=38)
tmail = TextField(label="البريد الالكتروني",rtl=True,height=38)
tphone = TextField(label="رقم الهاتف",rtl=True,height=38)
taddress = TextField(label="العنوان او مكان السكن",rtl=True,height=38)

############################################################################

###############################----- Marks ------#######################

marktext = Text("علامات الطالب",text_align="center",weight="bold",color="#004D40")
mathimatic = TextField(label="الرياضيات",width=110,rtl=True,height=38)
arabic = TextField(label="العربية",width=110,rtl=True,height=38)
france = TextField(label="الفرنسية",width=110,rtl=True,height=38)
english = TextField(label="الانجليزية",width=110,rtl=True,height=38)
art = TextField(label="الفنون",width=110,rtl=True,height=38)
chemistry = TextField(label="الكيمياء",width=110,rtl=True,height=38)

##############################################################################


################## ------------ Database ------------- #####################
coon = sqlite3.connect("studentdata.db",check_same_thread=False)

cursor = coon.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               stdname TEXT,
               stdmail TEXT,
               stdphone TEXT,
               stdaddress TEXT,
               stmathimatic INTEGER,
               starbic INTEGER,
               stfrance INTEGER,
               stenglish INTEGER,
               start INTEGER,
               stchemistry INTEGER)""")
coon.commit()
############################################################################

table_name = "student"
qyery = f"SELECT COUNT(*) FROM {table_name}"
cursor.execute(qyery)
result = cursor.fetchone()
row_count = result[0]
########## ---------------- Functions ---------------------- ###############

def format_entry(page):
    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdmail,stdphone,stdaddress,stmathimatic,starbic,stfrance,stenglish,start,stchemistry) VALUES(?,?,?,?,?,?,?,?,?,?)", (tname.value,tmail.value,tphone.value,taddress.value,mathimatic.value,arabic.value,france.value,english.value,art.value,chemistry.value))
        coon.commit()

    def show(e):
        page.clean()
        c = coon.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)  

        if not users == "":
            keys = ['id','stdname','stdmail','stdphone','stdaddress','stmathimatic','starbic','stfrance','stenglish','start','stchemistry']
            result = [dict(zip(keys,values)) for values in users]
            for x in result:
                ############### total_and_result ###############
                m = x["stmathimatic"]
                ar = x["starbic"]
                f = x["stfrance"]
                e = x["stenglish"]
                a = x["start"]
                c = x["stchemistry"]
                resu = m + ar + f + e + a + c

                if resu < 50 :
                    re = Text("😒 راسب",color="#FFFFFF",size=19)
                if resu > 50 :
                    re = Text("😁👍 ناجح",color="#FFFFFF",size=19)    


                page.add(
                    Card(
                        color="#004D40",
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading=Icon(name=icons.PERSON,color="#ffffff"),
                                    title=Text("Name : "+ x["stdname"],color="#FFFFFF"),
                                    subtitle = Text("Student Email : "+ x["stdmail"],color="#FFFFFF")
                                ),
                                Row([
                                    Text("Phone : "+ x["stdphone"],color="#FFFFFF",weight="bold"),
                                    Text("Address : "+ x["stdaddress"],color="#FFFFFF",weight="bold")
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("الرياضيات: "+ str(x["stmathimatic"]),color="#FFFFFF"),
                                    Text("العربية : "+ str(x["starbic"]),color="#FFFFFF"),
                                    Text("الفرنسية : "+ str(x["stfrance"]),color="#FFFFFF")
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("الانجليزية : "+ str(x["stenglish"]),color="#FFFFFF"),
                                    Text("الفنون : "+ str(x["start"]),color="#FFFFFF"),
                                    Text("الكيمياء : "+ str(x["stchemistry"]),color="#FFFFFF"),
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    re
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("")
                                ],alignment=MainAxisAlignment.CENTER)
                            ])
                        )
                    )
                )
                page.update()


##########################------------ ADD btn ------------###################

    addbutton = ElevatedButton(
    "اضافة نقاط الطالب",
    width=170,
    style=ButtonStyle(bgcolor="#D32F2F",
                      color="white",
                      padding=15),
                      on_click=add
                      )

    showbutton = ElevatedButton(
    "عرض كل الطلاب",
    width=170,
    style=ButtonStyle(bgcolor="#D32F2F",
                      color="white",
                      padding=15),
                      on_click=show
                      )    
############################################################################

    return Column(controls=[
        Container(content=Row(
            controls=[
                Text("ادخال بيانات الطالب",style="headlineMedium",color="#FFFFFF",weight="bold",size=30,text_align=...),
                IconButton(icons.ARROW_BACK,on_click=lambda _: page.go("/")),
            ],alignment=MainAxisAlignment.SPACE_AROUND
        ),padding=padding.all(10),bgcolor="#00796B",
        border_radius=border_radius.all(15),
        margin=margin.all(10)),
        Row([
            Image(src="logo.png",
                  width=200,
                  height=200)
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text("مرحبا بك ايها المعلم",
                 size=20,
                 weight="bold",
                 color="#004D40")
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text("عدد الطلاب المسجلين",
                 size=15,
                 color="#004D40"),
            Text(row_count,size=15,
                 color="#00796B",
                 weight="bold")     
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([
            tname,Icon(name=icons.PERSON,color="#00796B")
        ],alignment=MainAxisAlignment.CENTER,rtl=False),
        Row([
            tmail,Icon(name=icons.EMAIL,color="#00796B")
        ],alignment=MainAxisAlignment.CENTER,rtl=False),
        Row([
            tphone,Icon(name=icons.PHONE,color="#00796B")
        ],alignment=MainAxisAlignment.CENTER,rtl=False),
        Row([
            taddress,Icon(name=icons.LOCATION_CITY_OUTLINED,color="#00796B")
        ],alignment=MainAxisAlignment.CENTER,rtl=False),

        Row([
            marktext
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([
            mathimatic,
            arabic,
            france
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([
            english,
            art,
            chemistry
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([
            addbutton,
            showbutton
        ],alignment=MainAxisAlignment.CENTER,rtl=True)
    ])