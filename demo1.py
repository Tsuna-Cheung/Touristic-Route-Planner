import tkinter as tk
from tkinter import ttk
import EA_TRP as ea
import EA2_TRP as ea2
import MOEA_TRP as moea
from PIL import Image, ImageTk


class mainInterface(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Touristic Route Planner')
        self.root.resizable(0, 0)
        self.root.geometry('750x850')
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Top Frame
        self.topFrame = ttk.LabelFrame(self.root, text='Cities')
        self.secondFrame = ttk.LabelFrame(self.root, text='Introduction of city')
        self.topFrame.grid(column=0, row=0, padx=8, pady=4, sticky="ew")
        self.secondFrame.grid(column=0, row=1, padx=8, pady=4, sticky="nsew")
        self.checkbuttonList = []

        # Cities List
        # column 1
        self.var1 = tk.IntVar()
        self.r1 = tk.Checkbutton(self.topFrame, text='', variable=self.var1, onvalue=1, offvalue=0, bg='#EBEBEB')
        self.city1 = tk.Button(self.topFrame, text='1.Beijing 北京', bd=0, command=self.info_beijing)
        self.checkbuttonList.append(self.var1)
        self.var2 = tk.IntVar()
        self.r2 = tk.Checkbutton(self.topFrame, text='', variable=self.var2, onvalue=2, offvalue=0, bg='#EBEBEB')
        self.city2 = tk.Button(self.topFrame, text='2.Tianjin 天津', bd=0, command=self.info_tianjin)
        self.checkbuttonList.append(self.var2)
        self.var3 = tk.IntVar()
        self.r3 = tk.Checkbutton(self.topFrame, text='', variable=self.var3, onvalue=3, offvalue=0, bg='#EBEBEB')
        self.city3 = tk.Button(self.topFrame, text='3.ShiJiazhuang 石家庄', bd=0, command=self.info_shijiazhuang)
        self.checkbuttonList.append(self.var3)
        self.var4 = tk.IntVar()
        self.r4 = tk.Checkbutton(self.topFrame, text='', variable=self.var4, onvalue=4, offvalue=0, bg='#EBEBEB')
        self.city4 = tk.Button(self.topFrame, text='4.Taiyuan 太原', bd=0, command=self.info_taiyuan)
        self.checkbuttonList.append(self.var4)
        self.var5 = tk.IntVar()
        self.r5 = tk.Checkbutton(self.topFrame, text='', variable=self.var5, onvalue=5, offvalue=0, bg='#EBEBEB')
        self.city5 = tk.Button(self.topFrame, text='5.Hulunbuir 呼伦贝尔', bd=0, command=self.info_hulunbuir)
        self.checkbuttonList.append(self.var5)
        self.var6 = tk.IntVar()
        self.r6 = tk.Checkbutton(self.topFrame, text='', variable=self.var6, onvalue=6, offvalue=0, bg='#EBEBEB')
        self.city6 = tk.Button(self.topFrame, text='6.Shenyang 沈阳', bd=0, command=self.info_shenyang)
        self.checkbuttonList.append(self.var6)
        self.var7 = tk.IntVar()
        self.r7 = tk.Checkbutton(self.topFrame, text='', variable=self.var7, onvalue=7, offvalue=0, bg='#EBEBEB')
        self.city7 = tk.Button(self.topFrame, text='7.Changchun 长春', bd=0, command=self.info_changchun)
        self.checkbuttonList.append(self.var7)
        self.var8 = tk.IntVar()
        self.r8 = tk.Checkbutton(self.topFrame, text='', variable=self.var8, onvalue=8, offvalue=0, bg='#EBEBEB')
        self.city8 = tk.Button(self.topFrame, text='8.Harbin 哈尔滨', bd=0, command=self.info_harbin)
        self.checkbuttonList.append(self.var8)

        # column 2
        self.var9 = tk.IntVar()
        self.r9 = tk.Checkbutton(self.topFrame, text='', variable=self.var9, onvalue=9, offvalue=0, bg='#EBEBEB')
        self.city9 = tk.Button(self.topFrame, text='9.Shanghai 上海', bd=0, command=self.info_shanghai)
        self.checkbuttonList.append(self.var9)
        self.var10 = tk.IntVar()
        self.r10 = tk.Checkbutton(self.topFrame, text='', variable=self.var10, onvalue=10, offvalue=0, bg='#EBEBEB')
        self.city10 = tk.Button(self.topFrame, text='10.Nanjing 南京', bd=0, command=self.info_nanjing)
        self.checkbuttonList.append(self.var10)
        self.var11 = tk.IntVar()
        self.r11 = tk.Checkbutton(self.topFrame, text='', variable=self.var11, onvalue=11, offvalue=0, bg='#EBEBEB')
        self.city11 = tk.Button(self.topFrame, text='11.Hangzhou 杭州', bd=0, command=self.info_hangzhou)
        self.checkbuttonList.append(self.var11)
        self.var12 = tk.IntVar()
        self.r12 = tk.Checkbutton(self.topFrame, text='', variable=self.var12, onvalue=12, offvalue=0, bg='#EBEBEB')
        self.city12 = tk.Button(self.topFrame, text='12.Hefei 合肥', bd=0, command=self.info_hefei)
        self.checkbuttonList.append(self.var12)
        self.var13 = tk.IntVar()
        self.r13 = tk.Checkbutton(self.topFrame, text='', variable=self.var13, onvalue=13, offvalue=0, bg='#EBEBEB')
        self.city13 = tk.Button(self.topFrame, text='13.Xiamen 厦门', bd=0, command=self.info_xiamen)
        self.checkbuttonList.append(self.var13)
        self.var14 = tk.IntVar()
        self.r14 = tk.Checkbutton(self.topFrame, text='', variable=self.var14, onvalue=14, offvalue=0, bg='#EBEBEB')
        self.city14 = tk.Button(self.topFrame, text='14.Nanchang 南昌', bd=0, command=self.info_nanchang)
        self.checkbuttonList.append(self.var14)
        self.var15 = tk.IntVar()
        self.r15 = tk.Checkbutton(self.topFrame, text='', variable=self.var15, onvalue=15, offvalue=0, bg='#EBEBEB')
        self.city15 = tk.Button(self.topFrame, text='15.Qingdao 青岛', bd=0, command=self.info_qingdao)
        self.checkbuttonList.append(self.var15)
        self.var16 = tk.IntVar()
        self.r16 = tk.Checkbutton(self.topFrame, text='', variable=self.var16, onvalue=16, offvalue=0, bg='#EBEBEB')
        self.city16 = tk.Button(self.topFrame, text='16.Zhengzhou 郑州', bd=0, command=self.info_zhengzhou)
        self.checkbuttonList.append(self.var16)

        # column 3
        self.var17 = tk.IntVar()
        self.r17 = tk.Checkbutton(self.topFrame, text='', variable=self.var17, onvalue=17, offvalue=0, bg='#EBEBEB')
        self.city17 = tk.Button(self.topFrame, text='17.Wuhan 武汉', bd=0, command=self.info_wuhan)
        self.checkbuttonList.append(self.var17)
        self.var18 = tk.IntVar()
        self.r18 = tk.Checkbutton(self.topFrame, text='', variable=self.var18, onvalue=18, offvalue=0, bg='#EBEBEB')
        self.city18 = tk.Button(self.topFrame, text='18.Changsha 长沙', bd=0, command=self.info_changsha)
        self.checkbuttonList.append(self.var18)
        self.var19 = tk.IntVar()
        self.r19 = tk.Checkbutton(self.topFrame, text='', variable=self.var19, onvalue=19, offvalue=0, bg='#EBEBEB')
        self.city19 = tk.Button(self.topFrame, text='19.Guangzhou 广州', bd=0, command=self.info_guangzhou)
        self.checkbuttonList.append(self.var19)
        self.var20 = tk.IntVar()
        self.r20 = tk.Checkbutton(self.topFrame, text='', variable=self.var20, onvalue=20, offvalue=0, bg='#EBEBEB')
        self.city20 = tk.Button(self.topFrame, text='20.Guilin 桂林', bd=0, command=self.info_guilin)
        self.checkbuttonList.append(self.var20)
        self.var21 = tk.IntVar()
        self.r21 = tk.Checkbutton(self.topFrame, text='', variable=self.var21, onvalue=21, offvalue=0, bg='#EBEBEB')
        self.city21 = tk.Button(self.topFrame, text='21.Sanya 三亚', bd=0, command=self.info_sanya)
        self.checkbuttonList.append(self.var21)
        self.var22 = tk.IntVar()
        self.r22 = tk.Checkbutton(self.topFrame, text='', variable=self.var22, onvalue=22, offvalue=0, bg='#EBEBEB')
        self.city22 = tk.Button(self.topFrame, text='22.Chongqing 重庆', bd=0, command=self.info_chongqing)
        self.checkbuttonList.append(self.var22)
        self.var23 = tk.IntVar()
        self.r23 = tk.Checkbutton(self.topFrame, text='', variable=self.var23, onvalue=23, offvalue=0, bg='#EBEBEB')
        self.city23 = tk.Button(self.topFrame, text='23.Chengdu 成都', bd=0, command=self.info_chengdu)
        self.checkbuttonList.append(self.var23)
        self.var24 = tk.IntVar()
        self.r24 = tk.Checkbutton(self.topFrame, text='', variable=self.var24, onvalue=24, offvalue=0, bg='#EBEBEB')
        self.city24 = tk.Button(self.topFrame, text='24.Guiyang 贵阳', bd=0, command=self.info_guiyang)
        self.checkbuttonList.append(self.var24)

        # column 4
        self.var25 = tk.IntVar()
        self.r25 = tk.Checkbutton(self.topFrame, text='', variable=self.var25, onvalue=25, offvalue=0, bg='#EBEBEB')
        self.city25 = tk.Button(self.topFrame, text='25.Kunming 昆明', bd=0, command=self.info_kunming)
        self.checkbuttonList.append(self.var25)
        self.var26 = tk.IntVar()
        self.r26 = tk.Checkbutton(self.topFrame, text='', variable=self.var26, onvalue=26, offvalue=0, bg='#EBEBEB')
        self.city26 = tk.Button(self.topFrame, text='26.Lijiang 丽江', bd=0, command=self.info_lijiang)
        self.checkbuttonList.append(self.var26)
        self.var27 = tk.IntVar()
        self.r27 = tk.Checkbutton(self.topFrame, text='', variable=self.var27, onvalue=27, offvalue=0, bg='#EBEBEB')
        self.city27 = tk.Button(self.topFrame, text='27.Lhasa 拉萨', bd=0, command=self.info_lhasa)
        self.checkbuttonList.append(self.var27)
        self.var28 = tk.IntVar()
        self.r28 = tk.Checkbutton(self.topFrame, text='', variable=self.var28, onvalue=28, offvalue=0, bg='#EBEBEB')
        self.city28 = tk.Button(self.topFrame, text="28.Xi'an 西安", bd=0, command=self.info_xian)
        self.checkbuttonList.append(self.var28)
        self.var29 = tk.IntVar()
        self.r29 = tk.Checkbutton(self.topFrame, text='', variable=self.var29, onvalue=29, offvalue=0, bg='#EBEBEB')
        self.city29 = tk.Button(self.topFrame, text='29.Lanzhou 兰州', bd=0, command=self.info_lanzhou)
        self.checkbuttonList.append(self.var29)
        self.var30 = tk.IntVar()
        self.r30 = tk.Checkbutton(self.topFrame, text='', variable=self.var30, onvalue=30, offvalue=0, bg='#EBEBEB')
        self.city30 = tk.Button(self.topFrame, text='30.Xining 西宁', bd=0, command=self.info_xining)
        self.checkbuttonList.append(self.var30)
        self.var31 = tk.IntVar()
        self.r31 = tk.Checkbutton(self.topFrame, text='', variable=self.var31, onvalue=31, offvalue=0, bg='#EBEBEB')
        self.city31 = tk.Button(self.topFrame, text='31.Yinchuan 银川', command=self.info_yinchuan)
        self.checkbuttonList.append(self.var31)
        self.var32 = tk.IntVar()
        self.r32 = tk.Checkbutton(self.topFrame, text='', variable=self.var32, onvalue=32, offvalue=0, bg='#EBEBEB')
        self.city32 = tk.Button(self.topFrame, text='32.Ürümqi 乌鲁木齐', bd=0, command=self.info_urumqi)
        self.checkbuttonList.append(self.var32)

        self.bt = ttk.Button(self.topFrame, text='Plan your tour', command=self.get_route)
        self.bt.grid(row=9, column=0, sticky='we', rowspan=2, ipady=7, columnspan=2, pady=20)

        self.city_name = ttk.Label(self.secondFrame, text='', font=('Arial', 30))
        self.city_name.grid(row=0, column=0, padx=20, pady=8, sticky='w')

        self.sh = ttk.Separator(self.secondFrame, orient='horizontal')
        self.sh.grid(row=1, sticky="we", padx=20, columnspan=2, column=0)

        self.inner_frame1 = tk.Frame(self.secondFrame, width=700, bg='#EBEBEB', height=100)
        self.inner_frame1.grid(column=0, row=2, padx=20, sticky='we', pady=10)

        self.inner_frame2 = tk.Frame(self.secondFrame, bg='#EBEBEB', height=330)
        self.inner_frame2.grid(column=0, row=3, padx=20, sticky='we', pady=20)
        self.intro = tk.Message(self.secondFrame, text='',
                                width=700, bg='#EBEBEB')
        self.intro.grid(row=2, sticky='wn', ipadx=20, column=0)

        self.inner_leftFrame = tk.Frame(self.inner_frame2, width=250, height=330, bg='#EBEBEB')
        self.inner_leftFrame.grid(row=0, column=0, sticky='w')
        self.inner_rightFrame = tk.Frame(self.inner_frame2, width=480, height=330, bg='#EBEBEB')
        self.inner_rightFrame.grid(row=0, column=1, sticky='e', padx=40)
        self.canvas = tk.Canvas(self.inner_rightFrame, width=440, height=315, bg='#EBEBEB', bd=3)
        self.canvas.grid(row=0, column=1, sticky='we')
        self.lb = tk.Listbox(self.inner_leftFrame, bd=1, height=19, bg='#EBEBEB')
        self.lb.grid(row=0, column=0, sticky='w')
        self.lb.bind('<Double-1>', self.showimg)

    def list_arrang(self):
        self.r1.grid(row=1, column=0, sticky="w", padx=5)
        self.city1.grid(row=1, column=1, sticky="w")
        self.r2.grid(row=2, column=0, sticky="w", padx=5)
        self.city2.grid(row=2, column=1, sticky="w")
        self.r3.grid(row=3, column=0, sticky="w", padx=5)
        self.city3.grid(row=3, column=1, sticky="w")
        self.r4.grid(row=4, column=0, sticky="w", padx=5)
        self.city4.grid(row=4, column=1, sticky="w")
        self.r5.grid(row=5, column=0, sticky="w", padx=5)
        self.city5.grid(row=5, column=1, sticky="w")
        self.r6.grid(row=6, column=0, sticky="w", padx=5)
        self.city6.grid(row=6, column=1, sticky="w")
        self.r7.grid(row=7, column=0, sticky="w", padx=5)
        self.city7.grid(row=7, column=1, sticky="w")
        self.r8.grid(row=8, column=0, sticky="w", padx=5)
        self.city8.grid(row=8, column=1, sticky="w")

        # column 2
        self.r9.grid(row=1, column=2, sticky="w", padx=5)
        self.city9.grid(row=1, column=3, sticky="w")
        self.r10.grid(row=2, column=2, sticky="w", padx=5)
        self.city10.grid(row=2, column=3, sticky="w")
        self.r11.grid(row=3, column=2, sticky='w', padx=5)
        self.city11.grid(row=3, column=3, sticky="w")
        self.r12.grid(row=4, column=2, sticky="w", padx=5)
        self.city12.grid(row=4, column=3, sticky="w")
        self.r13.grid(row=5, column=2, sticky="w", padx=5)
        self.city13.grid(row=5, column=3, sticky="w")
        self.r14.grid(row=6, column=2, sticky="w", padx=5)
        self.city14.grid(row=6, column=3, sticky="w")
        self.r15.grid(row=7, column=2, sticky="w", padx=5)
        self.city15.grid(row=7, column=3, sticky="w")
        self.r16.grid(row=8, column=2, sticky='w', padx=5)
        self.city16.grid(row=8, column=3, sticky="w")

        # column 3
        self.r17.grid(row=1, column=4, sticky="w", padx=5)
        self.city17.grid(row=1, column=5, sticky="w")
        self.r18.grid(row=2, column=4, sticky="w", padx=5)
        self.city18.grid(row=2, column=5, sticky="w")
        self.r19.grid(row=3, column=4, sticky="w", padx=5)
        self.city19.grid(row=3, column=5, sticky="w")
        self.r20.grid(row=4, column=4, sticky="w", padx=5)
        self.city20.grid(row=4, column=5, sticky="w")
        self.r21.grid(row=5, column=4, sticky="w", padx=5)
        self.city21.grid(row=5, column=5, sticky="w")
        self.r22.grid(row=6, column=4, sticky="w", padx=5)
        self.city22.grid(row=6, column=5, sticky="w")
        self.r23.grid(row=7, column=4, sticky="w", padx=5)
        self.city23.grid(row=7, column=5, sticky="w")
        self.r24.grid(row=8, column=4, sticky="w", padx=5)
        self.city24.grid(row=8, column=5, sticky="w")

        # column 4
        self.r25.grid(row=1, column=6, sticky="w", padx=5)
        self.city25.grid(row=1, column=7, sticky="w")
        self.r26.grid(row=2, column=6, sticky="w", padx=5)
        self.city26.grid(row=2, column=7, sticky="w")
        self.r27.grid(row=3, column=6, sticky='w', padx=5)
        self.city27.grid(row=3, column=7, sticky="w")
        self.r28.grid(row=4, column=6, sticky="w", padx=5)
        self.city28.grid(row=4, column=7, sticky="w")
        self.r29.grid(row=5, column=6, sticky="w", padx=5)
        self.city29.grid(row=5, column=7, sticky="w")
        self.r30.grid(row=6, column=6, sticky="w", padx=5)
        self.city30.grid(row=6, column=7, sticky="w")
        self.r31.grid(row=7, column=6, sticky="w", padx=5)
        self.city31.grid(row=7, column=7, sticky="w")
        self.r32.grid(row=8, column=6, sticky='w', padx=5)
        self.city32.grid(row=8, column=7, sticky="w")

    def get_route(self):
        results = []
        for item in self.checkbuttonList:
            if item.get() != 0:
                results.append(item.get())
        c1 = getRoute_Interface(results)

    def info_beijing(self):
        self.city_name.config(text='Beijing')
        self.image = Image.open("img/beijing.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="Beijing is the capital of the People's Republic of China."
                 "With mountains surrounding the inland city on three sides, in addition to the old inner and outer city walls, Beijing was strategically poised and developed to be the residence of the emperor and thus was the perfect location for the imperial capital. The city is renowned for its opulent palaces, temples, parks, gardens, tombs, walls and gates."
                 "It has seven UNESCO World Heritage Sites—the Forbidden City, Temple of Heaven, Summer Palace, Ming Tombs, Zhoukoudian, and parts of the Great Wall and the Grand Canal— all tourist locations.")
        self.lb.delete(0, 'end')
        list_items = ['The Forbidden City', 'Temple of Heaven', 'Summer Palace', "The Bird's Nest",
                      'The Great Wall']
        for item in list_items:
            self.lb.insert('end', item)

    def info_tianjin(self):
        self.city_name.config(text='Tianjin')
        self.image = Image.open("img/tianjin.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/tianjin/
        self.intro.config(
            text="Tianjin is one of the four municipalities in China. Its name means 'the place where the emperor crossed the river'."
                 " Facing the Bohai Sea, the city, one time imperial port, serves as Beijing's vital gateway to the sea."
                 "In recent years it receives more and more attention from visitors due to its illustrious historical heritage and other natural resources. Blessed with variety of attractions,"
                 " this is a good place to explore. There are also many natural scenes of beauty as well as great historical events.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set((
                'The Yongle Bridge Tientsin Eye', 'Italian Style Street', 'Ancient cultural street', 'The Five Avenues',
                'Xikai Church',
                'Haihe River'))
        self.lb.config(listvariable=var)

    def info_shijiazhuang(self):
        self.city_name.config(text='Shijiazhuang')
        self.image = Image.open("img/shijiazhuang.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/hebei/shijiazhuang/
        self.intro.config(
            text="As the economic, political, cultural and scientific center of Hebei Province, Shijiazhuang is becoming more and more beautiful with recent urban development. "
                 "A jade-like moat  embraces the city gently, bordered by 20 charming parks. "
                 "This beautiful city is filled with culture and development, attracting visitors with new features daily. "
                 "Though it is a relatively young city, it is located on fertile land that boasts splendid cultural history."
                 " As such, the city is home to many significant cultural relics, such as the oldest stone-arch bridge in China,"
                 " Zhaozhou Bridge, and one of China's three hanging temples Qiaoloudian Hall (Bridge-Tower Hall).")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Zhaozhou Bridge', 'Cangyan Mountain', 'Bailin Temple', 'Bao Du Zhai'))
        self.lb.config(listvariable=var)

    def info_taiyuan(self):
        self.city_name.config(text='Taiyuan')
        self.image = Image.open("img/taiyuan.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/shanxi/taiyuan/
        self.intro.config(text="The city has a wealth of attractions and notably among these is the Jinci Temple."
                               " This is the city's most attractive temple although the Shuangta Si (Twin-Pagoda Temple) has become a symbol of the city on account of its unique architecture."
                               " Another major attraction is the Tianlong Shan Stone Caves where magnificent sculptures dating from the Tang Dynasty (618-907) may be seen. ")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Shanxi Museum', 'The Twin Towers', 'Jinci Temple'))
        self.lb.config(listvariable=var)

    def info_hulunbuir(self):
        self.city_name.config(text='Hulunbuir')
        self.image = Image.open("img/HulunBuir.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/inner_mongolia/hulunbeier/prairie.htm
        self.intro.config(text="Hulunbuir Prairie, or Hulun Buir Grassland, located in the northeast of Inner Mongolia,"
                               " is the superbly untouched prairie in China. Hulunbuir Prairie is among the three great prairies in the world,"
                               " termed “the kingdom of pasture”. The prairie covers  100 thousand sq km (39 thousand sq mi) of some 3,000 interwoven rivers and 500 dotted lakes."
                               " It is a pleasure for the eyes to see the land and what it holds. Place name Hulunbuir Prairie origins from the Hulun Lake and the Buir Lake."
                               " Hulun means otter and Buir means male otter in Mongolian, as the two lakes used to be teeming with otters.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Hulun Buir Grassland', 'Enhe Russia Nationality Township', 'Hulun Lake'))
        self.lb.config(listvariable=var)

    def info_shenyang(self):
        self.city_name.config(text='Shenyang')
        self.image = Image.open("img/shenyang.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/liaoning/shenyang/
        self.intro.config(text="As the largest city in Northeast China, it is the capital as well as political,"
                               " economic and cultural center of Liaoning Province. It is also an important industrial base and a famous historical city."
                               " Giving birth to the ancient Qing Dynasty, it has one of the country's two best preserved imperial palace complexes."
                               " The major attractions include International Ice and Snow Festival, September 18th Historical Museum and Xinglong Indoor Park & Glacier Zoological Paradise.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('The Shenyang Palace Museum', 'THE 918 HISTORICAL MUSEUM', "Marshal Zhang's Mansion Museum",
                 'ShengYang EXPO Garden'))
        self.lb.config(listvariable=var)

    def info_changchun(self):
        self.city_name.config(text='Changchun')
        self.image = Image.open("img/changchun.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/jilin/changchun/
        self.intro.config(text="It is undeniable that the place is a good travel destination."
                               " The natural sceneries lie in lakes and forests. Changbai Mountain, Nanhu Park (South Lake Park),"
                               " Jingyuetan National Forest Park are good places for you to enjoy the pleasure given by nature."
                               " Especially in winter the whole city will give you a real enjoyment of genuine winter. Besides,"
                               " there are colonial vestiges, such as Museum of the Imperial Palace of Manchukuo, Badabu."
                               " Still Changchun Film Studio, Jilin Provincial Museum, Capital Cities and Tombs of Ancient Koguryo Kingdom,"
                               " and Movie Wonderland provide you another different kind of enjoyment comparing with simply watching movies in cinemas.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Jingyuetan National Forest Park', 'Former site museum of CFS', 'South Lake Park',
                 'Changchun Movie Wonderland'))
        self.lb.config(listvariable=var)

    def info_harbin(self):
        self.city_name.config(text='Harbin')
        self.image = Image.open("img/harbin.png")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://chinatour.net/harbin-tour.html
        self.intro.config(
            text='Harbin, this name was originally a Manchu word meaning "a place for drying fishing nets"'
                 'Harbin grew from a small rural settlement on the Songhua River to become one of the largest cities in Northeast China.'
                 ' Having the most bitterly cold winters among major Chinese cities, Harbin is heralded as the Ice City for its well-known winter tourism and recreations.'
                 ' Harbin is notable for its beautiful ice sculpture festival in the winter.'
                 'The best place to go for Sightseeing in China in WINTER. Can also experience the worlds only snowfield high-speed railway')
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('St. Sophia Cathedral', 'Zhongyang Pedestrian Street', 'HARBIN ICE-SNOW WORLD', 'Songhua River'))
        self.lb.config(listvariable=var)

    def info_shanghai(self):
        self.city_name.config(text='Shanghai')
        self.image = Image.open("img/shanghai.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="Shanghai is China economic center. In the nearly 100 years from the 1870s to 1960s, has been the most prosperous city in the Far East.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('The Bund', 'City God Temple', 'Yu Garden', 'Lu Jia Zui'))
        self.lb.config(listvariable=var)

    def info_nanjing(self):
        self.city_name.config(text='Nanjing')
        self.image = Image.open("img/nanjing.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(text="Lying on the south bank of the Yangtze River, Nanjing, the capital of Jiangsu Province,"
                               " is one of the most delightful destinations in China. Known as the capital city of six or ten dynasties in ancient Chinese history,"
                               " it has a brilliant cultural heritage.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('The Memorial Hall of the victims in Nanjing Massacre by Japanese Invaders', 'Confucius Temple',
                 'Xuanwu Lake Park', 'Presidential Palace of Nanjing', 'The Sun Yat-sen Mausoleum'))
        self.lb.config(listvariable=var)

    def info_hangzhou(self):
        self.city_name.config(text='Hangzhou')
        self.image = Image.open("img/hangzhou.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text='Hangzhou has been one of the most renowned and affluent cities of China for the last millennium.'
                 ' A manufacturing hub, industrial city, Hangzhou is immortalized by several renowned poets and artists.'
                 ' The city has a lot of places rich in natural beauty such as the city’s West Lake.'
                 'European traveler Macro Polo admired Hangzhou as “the Most Splendid and Luxurious City in the World” and “The city of heaven”')
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('West Lake', 'Song Dynasty Town', 'LingYin Temple', 'Xixi Wetland Park', 'Leifeng Pagoda'))
        self.lb.config(listvariable=var)

    def info_hefei(self):
        self.city_name.config(text='Hefei')
        self.image = Image.open("img/hefei.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="Lying between the Yangtze River and Huaihe River, Hefei is the capital city of Anhui Province."
                 " Covering an area of 7,266 square kilometers (about 2,805 square miles),"
                 " it is the key tourist city of the whole province and the best place to know about the brilliant Anhui culture."
                 "It is a beautiful city with good surroundings - the Huaihe River flows to its north, to its south is Yangtze River,"
                 " and to its south- east lies the Chaohu Lake with its expansive blue waters. As is known, every city in China has a city tree and a city flower and,"
                 " in the case of this city,"
                 " the Yulan tree is its city tree and the sweet-scented osmanthus, pomegranate flower is its city flower.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Sanhe Ancient Town', 'Xiaoyao Ford'))
        self.lb.config(listvariable=var)

    def info_xiamen(self):
        self.city_name.config(text='Xiamen')
        self.image = Image.open("img/xiamen.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # wiki
        self.intro.config(text='Xiamen, or Amoy, is known for its mild climate, Hokkien culture and Gulangyu Island,'
                               ' as well as its relatively low pollution. In 2006, '
                               'Xiamen was ranked as Chinese second-"most suitable city for living", '
                               'as well as Chinese "most romantic leisure city" in 2011.'
                               'And University of Xiamen has the reputation of being the most beautiful university in China.')
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Kulangsu', 'University of Xiamen', 'Amoy Yat Sen Road'))
        self.lb.config(listvariable=var)

    def info_nanchang(self):
        self.city_name.config(text='Nanchang')
        self.image = Image.open("img/nanchang.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/jiangxi/nanchang/
        self.intro.config(
            text="The over 1000-year-old Pavilion of Prince Teng and the praised 'Essay on Pavilion of Prince Teng' ensure the fame of Nanchang,"
                 " the capital city of Jiangxi Province. The name of the city literally means 'a prosperous south part of China'"
                 "It is a beautiful city with the Gan River, the mother river of local people, traversing through the whole city."
                 " Water is her soul or in other words water carries all her beauty. Lakes and rivers in or around the city bring a special kind of charm to the city."
                 " It is honored as 'a green pearl in the southern part of China' thanks to its clear water, fresh air and great inner city virescence.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('TengWang Pavilion', 'Bayi Square'))
        self.lb.config(listvariable=var)

    def info_qingdao(self):
        self.city_name.config(text='Qingdao')
        self.image = Image.open("img/qingdao.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/shandong/qingdao/
        self.intro.config(
            text="Qingdao located in the southeast part of Shandong Province, is a beautiful seaside city with clear air and enchanting sea view. This city, bordered by the Yellow Sea on two sides,"
                 " has the largest bathing beach in Asia and produces the mellow Tsingtao Beer.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Zhan Qiao', 'Eight Great Passes', 'Laoshan', 'St.Michaels Cathedral'))
        self.lb.config(listvariable=var)

    def info_zhengzhou(self):
        self.city_name.config(text='Zhengzhou')
        self.image = Image.open("img/zhengzhou.png")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/henan/zhengzhou/
        self.intro.config(
            text="Zhengzhou is a national historical and cultural city and also the first destination for any Henan Tour. "
                 "The ancient city was the capital of Shang Dynasty (16th - 11th century BC) 3,500 years ago when porcelain and the Chinese technique of bronze smelting were comparatively more developed."
                 " A green ceramic glaze pot unearthed in Zhengzhou has been shown to be the most ancient porcelain in China."
                 "For anyone interested in Chinese ancient history and wishing to know more on it, Zhengzhou is one city that should not be missed.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Shaolin Temple', 'Pagoda Forest', 'Erqi Memorial Tower', 'Song Mountain'))
        self.lb.config(listvariable=var)

    def info_wuhan(self):
        self.city_name.config(text='Wuhan')
        self.image = Image.open("img/wuhan.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/wuhan.htm
        self.intro.config(
            text="Wuhan is a city with both an ancient history and a thriving present. Historic relics excavated from ancient tombs tell the city's long history dating back 3,500 years."
                 " In the period of Pre-Qin (770 B.C. - 221 B.C.), it was the land of the State of Chu (one of the seven warring states before Qin,"
                 " in the country's first feudal dynasty) and was the cradle of the brilliant Chu Civilization."
                 " Starting here, merchants followed the great Yangtze River and lake network to expand businesses throughout the entire country.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Yellow Crane Tower', 'Wuhan Yangtze River Bridge', 'East Lake'))
        self.lb.config(listvariable=var)

    def info_changsha(self):
        self.city_name.config(text='Changsha')
        self.image = Image.open("img/changsha.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/hunan/changsha/
        self.intro.config(
            text="Although not as ancient a capital city as Beijing, Nanjing or Xi'an, Changsha also has rich historical heritages including old wall remains,"
                 " tomb sites, religious temples and buildings. What earns the city its reputation among visitors are two things. One is a great man in recent history,"
                 " Chairman Mao Zedong and the other is Yuelu Academy, a time-honored academic school perched on the scenic Mt. Yuelu. Originally built in 976 during the Song Dynasty,"
                 " the academy school survived through the Yuan, Ming and Qing dynasties and is considered to be the cradle of Huxiang Culture, simply means the culture school in Hunan Province."
                 " Orange Isle, which is 1.2 miles (2 km) from the East Gate of Mt. Yuelu, is also worthy visiting.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('YueLu Mountain', 'Aiwan Ting Pavilion', 'Orange Isle'))
        self.lb.config(listvariable=var)

    def info_guangzhou(self):
        self.city_name.config(text='Guangzhou')
        self.image = Image.open("img/guangzhou.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(text="Guangzhou is the southern gateway to China in the traditional sense,"
                               " representative of the southern metropolis, also China's gourmet capital."
                               "Guangzhou, also known as Canton,is the capital and most populous city of the province of Guangdong in southern China."
                               "On the Pearl River about 120 km north-northwest of Hong Kong, Guangzhou has a history of over 2,200 years and was a major terminus of the maritime Silk Road, "
                               "and continues to serve as a major port and transportation hub, as well as one of China's Four largest cities.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Canton Tower', 'Shameen Island', 'Shishi Sacred Heart Cathedral', 'Baiyun Mountain'))
        self.lb.config(listvariable=var)

    def info_guilin(self):
        self.city_name.config(text='Guilin')
        self.image = Image.open("img/guilin.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # china tour.net
        self.intro.config(
            text='Its name means "Forest of Sweet Osmanthus". In China, the landscape of Guilin is synonymous with beautiful scenery.'
                 'As the famous Chinese saying goes “Guilin’s scenery is peerless in the world” , '
                 'Guilin has always been a popular tourist destination for people from both home and abroad. '
                 'Travelling in Guilin is a way of getting close to nature. With its unique karst landscape and charming hills, '
                 'rivers and terraces, Guilin is definitely a city worth exploring.')
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Li River', 'Longsheng Rice Terrace', 'Reed flute cave', 'Seven-star Park'))
        self.lb.config(listvariable=var)

    def info_sanya(self):
        self.city_name.config(text='Sanya')
        self.image = Image.open("img/sanya.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(text="The best place for Vacation in China in the WINTER."
                               "Also best destination for meeting chinese beauty ,but still sunshine!"
                               "The area has a tropical wet and dry climate,featuring very warm weather all year around. "
                               "Monsoonal influences are strong, with a relatively lengthy wet season and a pronounced dry season.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('WU ZHI ZHOU', 'Yalong Bay', 'The Remotest Corners of the Globe', 'Tropical Paradise Forest Park'))
        self.lb.config(listvariable=var)

    def info_chongqing(self):
        self.city_name.config(text='Chongqing')
        self.image = Image.open("img/chongqing.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/chongqing.htm
        self.intro.config(text="Chongqing is the largest municipality in southwest China. "
                               "It is a modern port city on the upper reaches of the Yangtze River at the confluence of the Yangtze and Jialing Rivers."
                               "The city attracts visitors from home and abroad for its natural wonders and cultural heritage."
                               " As a common starting port for the Yangtze River cruise,"
                               " tourists can go for a downstream tour to the magnificent Three Gorges.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Hong Ya Cave', 'Ciqikou ancient town', 'Three Natural Bridges Wulong County', 'Wanzhou Fall'))
        self.lb.config(listvariable=var)

    def info_chengdu(self):
        self.city_name.config(text='Chengdu')
        self.image = Image.open("img/chengdu.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/chengdu.htm
        self.intro.config(
            text="Chengdu, the capital of China's southwest Sichuan Province,  is famed for being the home of cute giant pandas."
                 "Traveling or living in Chengdu can be a great fun. Besides the amazing places of interest,"
                 " the city offers a lot inviting activities for visitors and expats. Sampling the famous Sichuan food is a must here."
                 " The hot and spicy dishes and varied tasty snacks are sure to whip up your appetite. Go shopping at the Chunxi Road,"
                 " spend a leisurely afternoon in a teahouse, and watch a Sichuan Opera performance at night "
                 "– this would be a perfect day giving you a deeper understanding of this charming city.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Chengdu Research Base of Giant Panda Breeding', 'WuHou Shrine', 'Dujiangyan', 'Jinli',
                 'The Wide and Narrow Lanes'))
        self.lb.config(listvariable=var)

    def info_guiyang(self):
        self.city_name.config(text='Guiyang')
        self.image = Image.open("img/guiyang.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="Guiyang, capital of Guizhou Province, is located in the southwest of China, on the eastern side of the Yunnan-Guizhou Plateau."
                 " It is a transfer point between most China cities, and the various ethnic minorities’ villages in the province."
                 " It is said that in ancient times, the city was surrounded by dense bamboo groves, and was famous for producing a musical instrument known as Zhu."
                 " Hence the city is also called Zhu for short.The city is renowned for its colorful culture,"
                 " represented by various ethnic groups and its special landform - Karst. Guiyang is home to more than 30 minority ethnic groups including,"
                 " Miao, Buyi, Dong and Hui.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(
            ('National urban wetland park of Huaxi', 'The Jiaxiu Pavilion', 'Qingyan Ancient Town', 'Qianling Park'))
        self.lb.config(listvariable=var)

    def info_kunming(self):
        self.city_name.config(text='Kunming')
        self.image = Image.open("img/kunming.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/kunming.htm
        self.intro.config(
            text="Kunming, capital of Yunnan Province, is known as 'the City of Eternal Spring' for its pleasant climate and flowers that bloom all year long."
                 " With a history of more than 2,400 years, it was the gateway to the celebrated Silk Road that facilitated trade with Tibet, Sichuan, Myanmar,"
                 " India and beyond. Today it is the provincial political, economical and cultural center of Yunnan as well as the most popular tourist destination in southwest China."
                 " The city is also the focal point of Yunnan minority culture. Some 26 ethnic minorities such as Yi, Bai, Miao, Dai, and Hani inhabit this region.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Dian Lake', 'Yunnan Nationalities village', 'World Horticultural Expo Garden', 'Jinma Biji',
                 'Stone Forest'))
        self.lb.config(listvariable=var)

    def info_lijiang(self):
        self.city_name.config(text='Lijiang')
        self.image = Image.open("img/lijiang.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/lijiang.htm
        self.intro.config(
            text="Lijiang, an attractive tourist destination in Yunnan Province, is considered a fairyland blessed with fresh air,"
                 " clear streams, breathtaking snowy mountains and an undisturbed landscape inhabited by friendly people."
                 " It exercises jurisdiction over four counties and an Old Town District. This is the main region inhabited by the Naxi People,"
                 " one of China's 55 minority ethnic groups. The Old Town District has the well preserved Lijiang Old Town,"
                 " listed a World Cultural Heritages site by UNESCO in 1997.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Old Town of Lijiang', 'Tiger Leaping Gorge', 'Shuhe Ancient Town', 'Lugu Lake',
                 'Jade Dragon Snow Mountain'))
        self.lb.config(listvariable=var)

    def info_lhasa(self):
        self.city_name.config(text='Lhasa')
        self.image = Image.open("img/lhasa.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="As the home of Tibetan Buddhism, Tibet has attracted more and more visitors with its mysterious culture and incredible scenery."
                 "There are magnificent snow mountains, clear lakes, boundless grassland and running rivers. Besides the beautiful natural landscape,"
                 " the mysterious culture has made it a holy land in many people’s heart.Lhasa is usually the first destination for people who travel to Tibet."
                 " It is very convenient to travel to other places from Lhasa.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Potala Palace', 'Jokhang Temple', 'Namtso'))
        self.lb.config(listvariable=var)

    def info_xian(self):
        self.city_name.config(text="Xi'an")
        self.image = Image.open("img/xian.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        self.intro.config(
            text="Anciently known as Chang'an(长安). China, known as the central state, began its period in Xi'an as her chief land."
                 "Xian, one of the most popular destinations in China, shines with its rich culture and history and has attracted more and more visitors."
                 "The history of civilization dates back to 7000 years ago. It has become a city in 3100 years ago."
                 " The city was the capital of 13 most glorious dynasties including Zhou, Qin, Han, Tang and so on.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Terracotta Army', 'Giant Wild Goose Pagoda', 'Huaqing Palace', 'The Xi’an Circumvallation'))
        self.lb.config(listvariable=var)

    def info_lanzhou(self):
        self.city_name.config(text='Lanzhou')
        self.image = Image.open("img/lanzhou.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/gansu/lanzhou/
        self.intro.config(
            text="Lanzhou is the capital city of Gansu Province in northwest China. The Yellow River, the Chinese Mother River,"
                 " runs through the city, ensuring rich crops of many juicy and fragrant fruits. Today, it is a hub of the Silk Road Tourism Ring,"
                 " with Maiji Caves to the east, Bingling Temple Grottoes to the west, Labrang Monastery to the south and Dunhuang Mogao Caves to the north."
                 "With mountains to the south and north of the city and the Yellow River flowing from the east to the west, "
                 "Lanzhou is a beautiful modern city with both the grand beauty of northern cities and the prettiness of southern cities.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Baita Mountain Park', 'Zhongshan Bridge', 'Gansu Provincial Museum', 'Statue Of Mother Yellow River'))
        self.lb.config(listvariable=var)

    def info_xining(self):
        self.city_name.config(text='Xining')
        self.image = Image.open("img/xining.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/qinghai/xining/
        self.intro.config(text="Xining is also called the Summer Resort Capital of China for its cool summer. "
                               "The region also provides a number of attractions making a visit to the area well worth considering."
                               " The scenery of the Qinghai Lake, provides an escape from fervent cities and allows you to experience beautiful natural sceneries."
                               " The lake itself is quite amazing. The Birds Island, situated on the northwest of Qinghai Lake,"
                               " is waiting to present you with an extensive array of birds. To the city's southwest, "
                               "is the birthplace of the founder of the Gelugpa Sect. The gem of the Tibetan culture- Kumbum Monastery was built here."
                               " To the north of Xining is the Northern Buddhist Temple. Climbing the temple will reward you with a view of the city from the mountaintop. ")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Riyue Mountain', 'Dongguan Mosque', "Ta'er Monastery"))
        self.lb.config(listvariable=var)

    def info_yinchuan(self):
        self.city_name.config(text='Yinchuan')
        self.image = Image.open("img/yinchuan.jpg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/ningxia/yinchuan/
        self.intro.config(text="A brilliant culture has contributed to Yinchuan being a famous tourist city."
                               " There are over 60 historical sites including mosques, pagodas, pavilions, temples,"
                               " and imperial tombs as well as natural scenery such as Helan Mountain, Sand Lake, and Shapotou."
                               "Yinchuan is a multi-nationality city including Han, Hui, Manchu, Mongolian, and Chaoxian peoples."
                               " Among them, the Hui people account for 26.3 percent of the total population and they have maintained the traditional folk customs and life style that are unique to other ethnic group.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('Western Xia Imperial Tombs', 'Rock Art Helan Mountain',
                 'The Park of Customs and Culture in the Homeland of Chinese Hui People', 'Shuidonggou Site',
                 'Drum Tower'))
        self.lb.config(listvariable=var)

    def info_urumqi(self):
        self.city_name.config(text='Ürümqi')
        self.image = Image.open("img/urumqi.jpeg")
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)
        # https://www.travelchinaguide.com/cityguides/urumqi.htm
        self.intro.config(text="Urumqi, the capital of Xinjiang Uygur Autonomous Region in northwest China, "
                               "is just like a piece of emerald embedded at the foot of the Tianshan Mountains. "
                               "As home to 49 minority ethnic groups, this graceful prairie city is an important stop along the ancient Silk Road, "
                               "leading to Central Asia and even as far as Europe."
                               "The city lies in the shadow of the lofty ice-capped Bogda Peak with vast Salt Lake to the east, "
                               "rolling pine-covered Southern Hill to the south, and alternating fields and sand dunes of Zunggar Basin to the northwest. "
                               "With shorter spring and autumn but longer winter and summer, May to October is the golden season for travel, "
                               "when flowers are in full bloom and the fruits, like melons and grape, are ripe with fragrance.")
        self.lb.delete(0, 'end')
        var = tk.StringVar()
        var.set(('TianShan Grand Canyon', 'Southern Pastures', 'Xinjiang International Grand Bazaar', 'Dabancheng'))
        self.lb.config(listvariable=var)

    def showimg(self, event):
        dir = './img/'
        fn = self.lb.get(self.lb.curselection())
        fn = fn.replace(" ", "_")
        path = dir + fn + '.jpeg'
        self.image = Image.open(path)
        self.image = self.image.resize((440, 315), Image.ANTIALIAS)
        self.im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(225, 165, image=self.im)


class getRoute_Interface(object):
    def __init__(self, l1):
        self.window = tk.Tk()
        self.window.title('Plan your tour')
        self.window.geometry('590x655')
        self.window.resizable(0, 0)
        self.cl = l1

        # Tab Control
        self.tabControl = ttk.Notebook(self.window)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='By Distance')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='By Cost')
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='By Both')
        self.tabControl.pack(expand=1, fill="both")

        # tab1
        self.frame_a = ttk.LabelFrame(self.tab1, text='Plan your tour')
        self.frame_a.grid(column=0, row=0, padx=8, pady=4)
        self.l11 = ttk.Label(self.frame_a, text="You've selected:")
        self.l11.grid(column=0, row=0, sticky='W')
        self.top_frame_a = tk.Frame(self.frame_a, width=500, height=70, bg='green')
        self.top_frame_a.grid(column=0, row=1, padx=8, pady=4)
        self.l12 = tk.Message(self.top_frame_a, text='',
                              width=500, bg='#EBEBEB')
        self.l12.grid(column=0, row=0, sticky='W')
        self.l13 = ttk.Label(self.frame_a, text="Departure:")
        self.l13.grid(column=0, row=2, sticky='W', pady=4)
        name_list = []
        for item in self.cl:
            name_list.append(self.code_to_name(item))
        self.cb1 = ttk.Combobox(self.frame_a, values=name_list)
        self.cb1.grid(column=0, row=3, sticky='W')
        self.cb1.current(0)
        self.bt1 = tk.Button(self.frame_a, text='Plan the Tour', command=self.tour_planning_a)
        self.bt1.grid(column=0, row=4, sticky='W', pady=4)

        # tab2
        self.frame_b = ttk.LabelFrame(self.tab2, text='Plan your tour')
        self.frame_b.grid(column=0, row=0, padx=8, pady=4)
        self.l21 = ttk.Label(self.frame_b, text="You've selected:")
        self.l21.grid(column=0, row=0, sticky='W')
        self.top_frame_b = tk.Frame(self.frame_b, width=500, height=70, bg='green')
        self.top_frame_b.grid(column=0, row=1, padx=8, pady=4)
        self.l22 = tk.Message(self.frame_b, text='',
                              width=500, bg='#EBEBEB')
        # self.l12 = ttk.Label(self.monty_a, text="", width=50)
        self.l22.grid(column=0, row=0, sticky='W')
        self.l23 = ttk.Label(self.frame_b, text="Departure:")
        self.l23.grid(column=0, row=2, sticky='W', pady=4)
        self.cb2 = ttk.Combobox(self.frame_b, values=name_list)
        self.cb2.grid(column=0, row=3, sticky='W')
        self.cb2.current(0)
        self.bt2 = tk.Button(self.frame_b, text='Plan the Tour', command=self.tour_planning_b)
        self.bt2.grid(column=0, row=4, sticky='W', pady=4)

        # tab3
        self.frame_c = ttk.LabelFrame(self.tab3, text='Plan your tour')
        self.frame_c.grid(column=0, row=0, padx=8, pady=4)
        self.l31 = ttk.Label(self.frame_c, text="You've selected:")
        self.l31.grid(column=0, row=0, sticky='W')
        self.top_frame_c = tk.Frame(self.frame_c, width=500, height=70, bg='green')
        self.top_frame_c.grid(column=0, row=1, padx=8, pady=4)
        self.l32 = tk.Message(self.frame_c, text='',
                              width=500, bg='#EBEBEB')
        self.print_selection()
        self.l32.grid(column=0, row=0, sticky='W')
        self.l33 = ttk.Label(self.frame_c, text="Departure:")
        self.l33.grid(column=0, row=2, sticky='W', pady=4)
        self.cb3 = ttk.Combobox(self.frame_c, values=name_list)
        self.cb3.grid(column=0, row=3, sticky='W')
        self.cb3.current(0)
        self.bt3 = tk.Button(self.frame_c, text='Plan the Tour', command=self.tour_planning_c)
        self.bt3.grid(column=0, row=4, sticky='W', pady=4)

    def print_selection(self):
        rs = []
        for item in self.cl:
            rs.append(self.code_to_name(item))
        list_txt = ",".join(rs)
        self.l12.config(text=list_txt)
        self.l22.config(text=list_txt)
        self.l32.config(text=list_txt)

    def tour_planning_a(self):
        self.monty_a1 = ttk.LabelFrame(self.tab1, text='Recommendation Route')
        self.monty_a1.grid(column=0, row=1, padx=8, pady=20, sticky='W')
        self.l14 = ttk.Label(self.monty_a1, text='Recommendation Route:')
        self.l14.grid(column=0, row=0, sticky='W')
        self.inner_frame_a1 = tk.Frame(self.monty_a1, width=500, height=70, bg='green')
        self.inner_frame_a1.grid(column=0, row=1, padx=8, pady=4)
        self.l15 = tk.Message(self.inner_frame_a1, text='Calculating......',
                              width=500, bg='#EBEBEB')
        self.l15.grid(column=0, row=0, sticky='W')
        departure = self.name_to_code(self.cb1.get())
        if departure != self.cl[0]:
            idx = self.cl.index(departure)
            temp = self.cl[0]
            self.cl[0] = departure
            self.cl[idx] = temp
        [best_distance, best_route] = ea.evolutionaryAlg(self.cl)
        result = str(best_distance) + ' km'
        name_list = []
        for item in best_route:
            name_list.append(self.code_to_name(item))
        name_list.append(self.code_to_name(self.cl[0]))
        txt = "->".join(name_list)

        self.l15.config(text=txt)
        self.l16 = ttk.Label(self.monty_a1, text='Distance:')
        self.l16.grid(column=0, row=2, sticky='W', pady=4)
        self.l17 = ttk.Label(self.monty_a1, text=result)
        self.l17.grid(column=0, row=3, sticky='W')

    def tour_planning_b(self):
        departure = self.name_to_code(self.cb2.get())
        if departure != self.cl[0]:
            idx = self.cl.index(departure)
            temp = self.cl[0]
            self.cl[0] = departure
            self.cl[idx] = temp
        [best_moneycost, best_route] = ea2.evolutionaryAlg(self.cl)
        result = str(best_moneycost) + ' CNY'
        self.monty_b1 = ttk.LabelFrame(self.tab2, text='Recommendation Route')
        self.monty_b1.grid(column=0, row=1, padx=8, pady=20, sticky='W')
        self.l24 = ttk.Label(self.monty_b1, text='Recommendation Route:')
        self.l24.grid(column=0, row=0, sticky='W')

        self.inner_frame_b1 = tk.Frame(self.monty_b1, width=500, height=70, bg='green')
        self.inner_frame_b1.grid(column=0, row=1, padx=8, pady=4)

        name_list = []
        for item in best_route:
            name_list.append(self.code_to_name(item))
        name_list.append(self.code_to_name(self.cl[0]))
        txt = "->".join(name_list)

        self.l25 = tk.Message(self.inner_frame_b1, text=txt,
                              width=500, bg='#EBEBEB')
        self.l25.grid(column=0, row=0, sticky='W')
        self.l26 = ttk.Label(self.monty_b1, text='Money Spend:')
        self.l26.grid(column=0, row=2, sticky='W', pady=4)
        self.l27 = ttk.Label(self.monty_b1, text=result)
        self.l27.grid(column=0, row=3, sticky='W')

    def tour_planning_c(self):
        departure = self.name_to_code(self.cb2.get())
        if departure != self.cl[0]:
            idx = self.cl.index(departure)
            temp = self.cl[0]
            self.cl[0] = departure
            self.cl[idx] = temp
        [best_solution, best_distance, best_moneycost] = moea.evolutionaryAlg(self.cl)
        result1 = str(best_moneycost) + ' CNY'
        result2 = str(best_distance) + ' km'
        self.monty_c1 = ttk.LabelFrame(self.tab3, text='Recommendation Route')
        self.monty_c1.grid(column=0, row=1, padx=8, pady=20, sticky='W')
        self.l34 = ttk.Label(self.monty_c1, text='Recommendation Route:')
        self.l34.grid(column=0, row=0, sticky='W')
        self.inner_frame_c1 = tk.Frame(self.monty_c1, width=500, height=70, bg='green')
        self.inner_frame_c1.grid(column=0, row=1, padx=8, pady=4)

        name_list = []
        for item in best_solution:
            name_list.append(self.code_to_name(item))
        name_list.append(self.code_to_name(self.cl[0]))
        txt = "->".join(name_list)

        self.l35 = tk.Message(self.inner_frame_c1, text=txt,
                              width=500, bg='#EBEBEB')
        self.l35.grid(column=0, row=0, sticky='W')
        self.l36 = ttk.Label(self.monty_c1, text='Money spend:')
        self.l36.grid(column=0, row=2, sticky='W')
        self.l37 = ttk.Label(self.monty_c1, text=result1)
        self.l37.grid(column=0, row=3, sticky='W')
        self.l38 = ttk.Label(self.monty_c1, text='Distance:')
        self.l38.grid(column=0, row=4, sticky='W')
        self.l39 = ttk.Label(self.monty_c1, text=result2)
        self.l39.grid(column=0, row=5, sticky='W')

    def code_to_name(self, code):
        l_city = ['Beijing', 'Tianjin', 'Shijiazhuang', 'Taiyuan', 'Hulunbuir', 'Shenyang', 'Changchun', 'Harbin',
                  'Shanghai', 'Nanjing', 'Hangzhou', 'Hefei', 'Xiamen', 'Nanchang', 'Qingdao', 'Zhengzhou', 'Wuhan',
                  'Changsha', 'Guangzhou', 'Guilin', 'Sanya', 'Chongqing', 'Chengdu', 'Guiyang', 'Kunming', 'Lijiang',
                  'Lhasa', 'Xian', 'Lanzhou', 'Xining', 'Yinchuan', 'Ürümqi']
        idx = code - 1
        return l_city[idx]

    def name_to_code(self, name):
        l_city = ['Beijing', 'Tianjin', 'Shijiazhuang', 'Taiyuan', 'Hulunbuir', 'Shenyang', 'Changchun', 'Harbin',
                  'Shanghai', 'Nanjing', 'Hangzhou', 'Hefei', 'Xiamen', 'Nanchang', 'Qingdao', 'Zhengzhou', 'Wuhan',
                  'Changsha', 'Guangzhou', 'Guilin', 'Sanya', 'Chongqing', 'Chengdu', 'Guiyang', 'Kunming', 'Lijiang',
                  'Lhasa', 'Xian', 'Lanzhou', 'Xining', 'Yinchuan', 'Ürümqi']
        for i in range(len(l_city)):
            if name == l_city[i]:
                print('code:', i + 1)
                return (i + 1)


def main():
    M = mainInterface()
    M.list_arrang()
    tk.mainloop()


if __name__ == '__main__':
    main()
