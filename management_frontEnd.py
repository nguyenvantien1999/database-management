from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time
import management_backEnd

class Home:

    def __init__(self, root):
        self.root = root
        self.root.title("Database Management Systems")
        self.root.geometry("1365x750+260+100")
        self.root.config(bg="#b3ffb3")

        #========================================================Function========================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno('Database Management Systems', 'Xác nhận nếu bạn muốn thoát')
            if iExit > 0:
                root.destroy()
                return
        def HoaDonFn():
            root.destroy()
            rootHoaDon = Tk()
            application = HoaDon(rootHoaDon)
            rootHoaDon.mainloop()

        def HangHoaFn():
            root.destroy()
            rootHangHoa = Tk()
            application = HangHoa(rootHangHoa)
            rootHangHoa.mainloop()
            
        def KhachHangFn():
            root.destroy()
            rootKhachHang = Tk()
            application = KhachHang(rootKhachHang)
            rootKhachHang.mainloop()
        #=========================================================Frames=========================================================
        MainFrame = Frame(self.root, bg="#b3ffb3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#ccffff", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Database Management Systems", fg="green", bg="#ccffff")
        self.lblTit.grid(row=0, columnspan=4)

        self.lbl1Tit = Label(TitFrame, font=('arial', 12, 'italic'), text="© Nguyễn Văn Tiến - MSSV: 59132605", fg='blue', bg="#ccffff")
        self.lbl1Tit.grid(row=1, column=3)

        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM, pady=20, padx=20)

        DataFrame = Frame(DataFrame2, bd=1, width=1300, height=400, padx=20, pady=15, bg="#f2f2f2", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        #=========================================================Button=========================================================

        self.btnXuatBan = Button(DataFrame, text="ⓈⒶⓁⒺ\nHóa Đơn", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13, command=HoaDonFn)
        self.btnXuatBan.grid(row=0, column=0, padx=20, pady=10)

        self.btnGhiNo = Button(DataFrame, text="✎✎✎\nGhi nợ", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13)
        self.btnGhiNo.grid(row=0, column=1, padx=20, pady=10)

        self.btnHangHoa = Button(DataFrame, text="⌨⌨⌨\nDanh mục\nhàng hóa", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13, command=HangHoaFn)
        self.btnHangHoa.grid(row=0, column=2, padx=20, pady=10)

        self.btnXuatBan = Button(DataFrame, text="〠〠〠\nDanh mục\nkhách hàng", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13, command=KhachHangFn)
        self.btnXuatBan.grid(row=0, column=3, padx=20, pady=10)
            #------------------------------hàng 2--------------------------------
        self.btnCongTy = Button(DataFrame, text="☖☖☖\nDanh mục\ncông ty", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13)
        self.btnCongTy.grid(row=1, column=0, padx=20, pady=10)

        self.btnTaiKhoan = Button(DataFrame, text="☏☏☏\nKhu vực\nlưu trữ", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13)
        self.btnTaiKhoan.grid(row=1, column=1, padx=20, pady=10)

        self.btnThuNhap = Button(DataFrame, text="$$$\nTổng thu nhập\ntrên tháng", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13)
        self.btnThuNhap.grid(row=1, column=2, padx=20, pady=10)

        self.btnTaiKhoan = Button(DataFrame, text="➱➱➱\nQuản lý\ntài khoản", font=('arial', 25, 'bold'), bg="#2eb82e", fg="Ghost White", height=5, width=13)
        self.btnTaiKhoan.grid(row=1, column=3, padx=20, pady=10)
            #------------------------------hàng 3--------------------------------
        self.btnThoat = Button(text="Thoát", font=('arial', 12, 'bold'), bg='red', height=1, width=7, command=iExit)
        self.btnThoat.place(x=1265, y=698)

        self.btnCaiDat = Button(text="Cài đặt", font=('arial', 12, 'bold'), bg='#ffff66', height=1, width=7)
        self.btnCaiDat.place(x=1180, y=698)

        self.btnTroGiup = Button(text="Trợ giúp", font=('arial', 12, 'bold'), bg='#ffff66', height=1, width=7)
        self.btnTroGiup.place(x=1095, y=698)
#////////////////////////////////////////////END HOME///////////////////////////////////////////////
class HangHoa:
    
    def __init__(self, root):
        
        self.root = root
        self.root.title("Database Management Systems")
        self.root.geometry("1218x896+350+65")
        self.root.config(bg="#b3ffb3")
        global intSoLuong
        hangID = StringVar()
        tenHang = StringVar()
        DVTinh = StringVar()
        SoLuong = StringVar()
        intSoLuong = SoLuong.get()
        if intSoLuong != "":
            intSoLuong = int(SoLuong)
        donGiaNhap = StringVar()
        donGiaBan =StringVar()
        nhaCungCap = StringVar()
        txtUnitGrades = StringVar()
        DateIssued = StringVar()

        #========================================================Function========================================================
        def HomeFn():
            root.destroy()
            rootHome = Tk()
            application = Home(rootHome)
            rootHome.mainloop()

        def Cleartxt():
            hangID.set('')
            tenHang.set('')
            DVTinh.set('')
            SoLuong.set('')
            donGiaNhap.set('')
            donGiaBan.set('')
            nhaCungCap.set('')

        def Clear():
            Cleartxt()
            self.txtUnitGrades.delete('1.0', END)

        def addNew():
            DateIssued.set(time.strftime('%d/%m/%Y'))
            self.txtUnitGrades.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtUnitGrades.insert(END, 'Mã hàng:\t'+ hangID.get()+ '\t\t\t\t' + DateIssued.get()+'\n')
            self.txtUnitGrades.insert(END,'=====================================================')
            self.txtUnitGrades.insert(END,'Tên hàng:\t\t\t\t\t'+ tenHang.get()+'\n')
            self.txtUnitGrades.insert(END,'Đơn vị tính:\t\t\t\t\t'+ DVTinh.get()+'\n')
            self.txtUnitGrades.insert(END,'Số lượng:\t\t\t\t\t'+ SoLuong.get()+'\n')
            self.txtUnitGrades.insert(END,'Đơn giá bán:\t\t\t\t\t'+ donGiaBan.get()+'VNĐ\n')
            self.txtUnitGrades.insert(END,'Đơn giá nhập:\t\t\t\t\t'+ donGiaNhap.get()+'VNĐ\n')
            self.txtUnitGrades.insert(END,'Nhà cung cấp:\t\t\t\t\t'+ nhaCungCap.get()+'\n')
            self.txtUnitGrades.insert(END,'=====================================================')
            self.txtUnitGrades.insert(END,'\n\n\n\n\n\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        #====================================================DataBase Function====================================================
        def addData():
            if(len(hangID.get())!=0):
                addNew()
                management_backEnd.addNewRec(hangID.get(), tenHang.get(), DVTinh.get(), SoLuong.get(), donGiaNhap.get(), donGiaBan.get(), nhaCungCap.get())
                hangHoaList.delete(0,END)
                hangHoaList.insert(END,(hangID.get(), tenHang.get(), DVTinh.get(), SoLuong.get(), donGiaNhap.get(), donGiaBan.get(), nhaCungCap.get()))
                Cleartxt()
                

        def DisplayData():
            hangHoaList.delete(0,END)
            for row in management_backEnd.viewData():
                hangHoaList.insert(END, row)
                
        def hangRec(event):
            global sd 
            searchHang = hangHoaList.curselection()[0]
            sd = hangHoaList.get(searchHang)
            
            self.txtHangID.delete(0, END)
            self.txtHangID.insert(END, sd[1])
            self.txtTenHang.delete(0, END)
            self.txtTenHang.insert(END, sd[2])  
            self.txtDVTinh.delete(0, END)
            self.txtDVTinh.insert(END, sd[3])
            self.txtSL.delete(0, END)
            self.txtSL.insert(END, sd[4])
            self.txtdonGiaNhap.delete(0, END)
            self.txtdonGiaNhap.insert(END, sd[5])
            self.txtdonGiaBan.delete(0, END)
            self.txtdonGiaBan.insert(END, sd[6])
            self.txtnhaCungCap.delete(0, END)
            self.txtnhaCungCap.insert(END, sd[7])

            self.txtUnitGrades.delete('1.0', END)
            self.txtUnitGrades.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtUnitGrades.insert(END, 'Mã hàng:\t'+ sd[1] + '\n')
            self.txtUnitGrades.insert(END,'=====================================================')
            self.txtUnitGrades.insert(END,'Tên hàng:\t\t\t\t\t'+ sd[2]+'\n')
            self.txtUnitGrades.insert(END,'Đơn vị tính:\t\t\t\t\t'+ sd[3] +'\n')
            self.txtUnitGrades.insert(END,'Số lượng:\t\t\t\t\t'+ sd[4] + ' ' + sd[3] +'\n')
            self.txtUnitGrades.insert(END,'Đơn giá bán:\t\t\t\t\t'+ sd[5]+'VNĐ\n')
            self.txtUnitGrades.insert(END,'Đơn giá nhập:\t\t\t\t\t'+ sd[6]+'VNĐ\n')
            self.txtUnitGrades.insert(END,'Nhà cung cấp:\t\t\t\t\t'+ sd[7]+'\n')
            self.txtUnitGrades.insert(END,'=====================================================')
            self.txtUnitGrades.insert(END,'\n\n\n\n\n\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        def deleteData():
            if(len(hangID.get())!=0):
                management_backEnd.deleteDataRec(sd[0])
                Clear()
                DisplayData()
        
        def SearchData():
            hangHoaList.delete(0,END)
            for row in management_backEnd.searchDataRec(hangID.get(), tenHang.get(), DVTinh.get(), SoLuong.get(), donGiaNhap.get(), \
                donGiaBan.get(), nhaCungCap.get()):
                hangHoaList.insert(END, row)

        def update():
            if(len(hangID.get())!=0):
                management_backEnd.deleteDataRec(sd[0])
            if(len(hangID.get())!=0):
                management_backEnd.addNewRec(hangID.get(), tenHang.get(), DVTinh.get(), SoLuong.get(), donGiaNhap.get(), \
                donGiaBan.get(), nhaCungCap.get())
                hangHoaList.delete(0,END)
                hangHoaList.insert(END,(hangID.get(), tenHang.get(), DVTinh.get(), SoLuong.get(), donGiaNhap.get(), donGiaBan.get(), nhaCungCap.get()))
        #=========================================================Frames==========================================================

        MainFrame = Frame(self.root, bg="#b3ffb3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#ccffff", relief=RIDGE)
        TitFrame.pack(side=TOP, pady=5)
        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Danh mục hàng hóa", fg="green", bg="#ccffff")
        self.lblTit.grid(row=0, columnspan=4)

        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ListFrame = Frame(DataFrame2, bd=2, width=1300, height=210, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ListFrame.pack(side=TOP)
        ButtonFrame = Frame(DataFrame2, bd=2, width=1300, height=60, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='cadet blue')
        DataFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=400, padx=20, relief=RIDGE, bg='Ghost white', font=('Arial', 18, 'bold'), text='Chi tiết\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=400, padx=31, pady=3, relief=RIDGE, bg='powder blue', font=('Arial', 18, 'bold'), text='Unit Grades\n')
        DataFrameRIGHT.pack(side=RIGHT)

        #=========================================================Widget=========================================================

        self.lblHangID = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Mã hàng hóa:', padx=2, pady=2, bg='Ghost white')
        self.lblHangID.grid(row=0, column=0, sticky=W)
        self.txtHangID = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=hangID, bg='Ghost white', width=40)
        self.txtHangID.grid(row=0, column=1)

        self.lblTenHang = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Tên hàng:', padx=2, pady=2, bg='Ghost white')
        self.lblTenHang.grid(row=1, column=0, sticky=W)
        self.txtTenHang = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=tenHang, bg='Ghost white', width=40)
        self.txtTenHang.grid(row=1, column=1)

        self.lblDVTinh = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Đơn vị tính:', padx=2, pady=2, bg='Ghost white')
        self.lblDVTinh.grid(row=2, column=0, sticky=W)
        self.txtDVTinh = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=DVTinh, bg='Ghost white', width=40)
        self.txtDVTinh.grid(row=2, column=1)

        self.lblSL = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Số lượng:', padx=2, pady=2, bg='Ghost white')
        self.lblSL.grid(row=3, column=0, sticky=W)
        self.txtSL = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=SoLuong, bg='Ghost white', width=40)
        self.txtSL.grid(row=3, column=1)

        self.lbldonGiaNhap = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Đơn giá nhập:', padx=2, pady=2, bg='Ghost white')
        self.lbldonGiaNhap.grid(row=4, column=0, sticky=W)
        self.txtdonGiaNhap = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=donGiaNhap, bg='Ghost white', width=40)
        self.txtdonGiaNhap.grid(row=4, column=1)

        self.lbldonGiaBan = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Đơn giá bán:', padx=2, pady=2, bg='Ghost white')
        self.lbldonGiaBan.grid(row=5, column=0, sticky=W)
        self.txtdonGiaBan = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=donGiaBan, bg='Ghost white', width=40)
        self.txtdonGiaBan.grid(row=5, column=1)

        self.lblnhaCungCap = Label(DataFrameLEFT, font=('Arial', 14, 'bold'), text='Nhà cung cấp:', padx=2, pady=2, bg='Ghost white')
        self.lblnhaCungCap.grid(row=6, column=0, sticky=W)
        self.txtnhaCungCap = Entry(DataFrameLEFT, font=('Arial', 14, 'bold'), textvariable=nhaCungCap, bg='Ghost white', width=40)
        self.txtnhaCungCap.grid(row=6, column=1)

        #==================Khoản trắng==========================
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=7, columnspan=2)
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=8, columnspan=2)
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=9, columnspan=2)
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=10, columnspan=2)
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=11, columnspan=2)
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=12, columnspan=2, pady=8)
        #========================================================

        #===============================================UnitGrades==================================================================

        self.txtUnitGrades = Text(DataFrameRIGHT, height=19, width=60, bd=1, font=('arial', 11, 'bold'))
        self.txtUnitGrades.grid(row=0, column=0)

        #================================================ListFrame==================================================================

        lblNull = Label(ListFrame, bg='powder blue')
        lblNull.grid(row=0, column=0, pady=2)

        # header table
        lblSTT = Label(ListFrame, font=('Arial', 11, 'bold'), text='STT', padx=35, pady=2, bg='Ghost white')
        lblSTT.place(x=10, y=1)

        lblHangID = Label(ListFrame, font=('Arial', 11, 'bold'), text='Mã hàng', padx=35, pady=2, bg='Ghost white')
        lblHangID.place(x=115, y=1)

        lblTenHang = Label(ListFrame, font=('Arial', 11, 'bold'), text='Tên hàng', padx=60, pady=2, bg='Ghost white')
        lblTenHang.place(x=250, y=1)

        lblDVTinh = Label(ListFrame, font=('Arial', 11, 'bold'), text='Đơn vị tính', padx=45, pady=2, bg='Ghost white')
        lblDVTinh.place(x=442, y=1)

        lblSL = Label(ListFrame, font=('Arial', 11, 'bold'), text='Số lượng', padx=40, pady=2, bg='Ghost white')
        lblSL.place(x=616, y=1)

        lbldonGiaBan = Label(ListFrame, font=('Arial', 11, 'bold'), text='Giá bán', padx=45, pady=2, bg='Ghost white')
        lbldonGiaBan.place(x=768, y=1)

        lblnhaCungCap = Label(ListFrame, font=('Arial', 11, 'bold'), text='Nhà cung cấp', padx=45, pady=2, bg='Ghost white')
        lblnhaCungCap.place(x=917, y=1)

        scrollbar = Scrollbar(ListFrame)
        scrollbar.grid(row=1, column=1, sticky= 'ns')

        hangHoaList = Listbox(ListFrame, width=122, height=9, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        hangHoaList.bind('<<ListboxSelect>>', hangRec)
        hangHoaList.grid(row=1, column=0, padx=8)
        scrollbar.config(command=hangHoaList.yview)

        #================================================ButtonFrame=================================================================

        self.btnAddData = Button(ButtonFrame, text='Thêm', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=5, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text='Hiển thị', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text='Dọn dẹp', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=Clear)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Xóa', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text='Tìm kiếm', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=SearchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text='Cập nhật', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnComeBack = Button(ButtonFrame, text='Quay lại', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=5, command=HomeFn)
        self.btnComeBack.grid(row=0, column=6)
#////////////////////////////////////////////END HÀNG HÓA///////////////////////////////////////////
class KhachHang:

    def __init__(self, root):
        self.root = root
        self.root.title("Database Management Systems")
        self.root.geometry("1218x896+350+65")
        self.root.config(bg="#b3ffb3")

        KhachID = StringVar()
        tenKhach = StringVar()
        gioiTinh = StringVar()
        nhomKhach = StringVar()
        diaChiKhach = StringVar()
        SDTKhach = StringVar()
        emailKhach = StringVar()
        ghiChu = StringVar()
        txtDisplay = StringVar()
        DateIssued = StringVar()
        #========================================================Function========================================================
        def HomeFn():
            root.destroy()
            rootHome = Tk()
            application = Home(rootHome)
            rootHome.mainloop()

        def Cleartxt():
            KhachID.set('')
            tenKhach.set('')
            gioiTinh.set('')
            nhomKhach.set('')
            diaChiKhach.set('')
            SDTKhach.set('')
            emailKhach.set('')
            ghiChu.set('')

        def Clear():
            Cleartxt()
            self.txtDisplay.delete('1.0', END)

        def addNew():
            DateIssued.set(time.strftime('%d/%m/%Y'))
            self.txtDisplay.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtDisplay.insert(END, 'Mã khách hàng:\t'+ KhachID.get()+ '\t\t\t\t' + DateIssued.get()+'\n')
            self.txtDisplay.insert(END,'=====================================================\n')
            self.txtDisplay.insert(END,'Tên khach hàng:\t\t\t\t\t'+ tenKhach.get()+'\n')
            self.txtDisplay.insert(END,'Giới tính:\t\t\t\t\t'+ gioiTinh.get()+'\n')
            self.txtDisplay.insert(END,'Nhóm khách hàng:\t\t\t\t\t'+ nhomKhach.get()+'\n')
            self.txtDisplay.insert(END,'Địa chỉ khách hàng:\t\t\t\t\t'+ diaChiKhach.get()+'\n')
            self.txtDisplay.insert(END,'Số điện thoại:\t\t\t\t\t'+ SDTKhach.get()+'\n')
            self.txtDisplay.insert(END,'Email:\t\t\t\t\t'+ emailKhach.get()+'\n')
            self.txtDisplay.insert(END,'Ghi chu:\t\t\t\t\t'+ ghiChu.get()+'\n')
            self.txtDisplay.insert(END,'=====================================================')
            self.txtDisplay.insert(END,'\n\n\n\n\n\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        #====================================================DataBase Function====================================================
        def addData():
            addNew()
            if(len(KhachID.get())!=0):
                management_backEnd.addKhachHangNewRec(KhachID.get(), tenKhach.get(), gioiTinh.get(), nhomKhach.get(), diaChiKhach.get(), SDTKhach.get(), emailKhach.get(),ghiChu.get())
                khachList.delete(0,END)
                khachList.insert(END,(KhachID.get(), tenKhach.get(), gioiTinh.get(), nhomKhach.get(), diaChiKhach.get(), SDTKhach.get(), emailKhach.get(), ghiChu.get()))
            Cleartxt()

        def DisplayData():
            khachList.delete(0,END)
            for row in management_backEnd.viewKHData():
                khachList.insert(END, row)

        def khachRec(event):
            global sd1 
            searchKhach = khachList.curselection()[0]
            sd1 = khachList.get(searchKhach)
            
            self.txtKhachID.delete(0, END)
            self.txtKhachID.insert(END, sd1[1])
            self.txtTenKhach.delete(0, END)
            self.txtTenKhach.insert(END, sd1[2])  
            self.txtGioiTinh.delete(0, END)
            self.txtGioiTinh.insert(END, sd1[3])
            self.txtNhomKhach.delete(0, END)
            self.txtNhomKhach.insert(END, sd1[4])
            self.txtDiaChi.delete(0, END)
            self.txtDiaChi.insert(END, sd1[5])
            self.txtSDTKhach.delete(0, END)
            self.txtSDTKhach.insert(END, sd1[6])
            self.txtEmailKhach.delete(0, END)
            self.txtEmailKhach.insert(END, sd1[7])
            self.txtGhiChuKhach.delete(0, END)
            self.txtGhiChuKhach.insert(END, sd1[8])

            self.txtDisplay.delete('1.0', END)
            self.txtDisplay.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtDisplay.insert(END, 'Mã khách hàng:\t'+ KhachID.get()+ '\t\t\t\t' + DateIssued.get()+'\n')
            self.txtDisplay.insert(END,'=====================================================\n')
            self.txtDisplay.insert(END,'Tên khach hàng:\t\t\t\t\t'+ tenKhach.get()+'\n')
            self.txtDisplay.insert(END,'Giới tính:\t\t\t\t\t'+ gioiTinh.get()+'\n')
            self.txtDisplay.insert(END,'Nhóm khách hàng:\t\t\t\t\t'+ nhomKhach.get()+'\n')
            self.txtDisplay.insert(END,'Địa chỉ khách hàng:\t\t\t\t\t'+ diaChiKhach.get()+'\n')
            self.txtDisplay.insert(END,'Số điện thoại:\t\t\t\t\t'+ SDTKhach.get()+'\n')
            self.txtDisplay.insert(END,'Email:\t\t\t\t\t'+ emailKhach.get()+'\n')
            self.txtDisplay.insert(END,'Ghi chu:\t\t\t\t\t'+ ghiChu.get()+'\n')
            self.txtDisplay.insert(END,'=====================================================')
            self.txtDisplay.insert(END,'\n\n\n\n\n\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        def deleteData():
            if(len(KhachID.get())!=0):
                management_backEnd.deleteKHDataRec(sd1[0])
                Clear()
                DisplayData()

        def SearchData():
            khachList.delete(0,END)
            for row in management_backEnd.searchKHDataRec(KhachID.get(), tenKhach.get(), gioiTinh.get(), nhomKhach.get(), \
                diaChiKhach.get(), SDTKhach.get(), emailKhach.get(), ghiChu.get()):
                khachList.insert(END, row)

        def update():
            if(len(KhachID.get())!=0):
                management_backEnd.deleteKHDataRec(sd1[0])
            if(len(KhachID.get())!=0):
                management_backEnd.addKhachHangNewRec(KhachID.get(), tenKhach.get(), gioiTinh.get(), nhomKhach.get(), \
                diaChiKhach.get(), SDTKhach.get(), emailKhach.get(), ghiChu.get())
                khachList.delete(0,END)
                khachList.insert(END,(KhachID.get(), tenKhach.get(), gioiTinh.get(), nhomKhach.get(), \
                diaChiKhach.get(), SDTKhach.get(), emailKhach.get(), ghiChu.get()))
        #=========================================================Frames==========================================================

        MainFrame = Frame(self.root, bg="#b3ffb3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#ccffff", relief=RIDGE)
        TitFrame.pack(side=TOP, pady=5)
        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Danh mục khách hàng", fg="green", bg="#ccffff")
        self.lblTit.grid(row=0, columnspan=4)

        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ListFrame = Frame(DataFrame2, bd=2, width=1300, height=210, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ListFrame.pack(side=TOP)
        ButtonFrame = Frame(DataFrame2, bd=2, width=1300, height=60, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='cadet blue')
        DataFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=400, padx=20, relief=RIDGE, bg='Ghost white', font=('Arial', 18, 'bold'), text='Chi tiết\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=400, padx=31, pady=3, relief=RIDGE, bg='powder blue', font=('Arial', 18, 'bold'), text='Display\n')
        DataFrameRIGHT.pack(side=RIGHT)

        #=========================================================Widget=========================================================

        self.lblKhachID = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Mã khách hàng:", padx=2, pady=2, bg='Ghost white')
        self.lblKhachID.grid(row=0, column=0, sticky=W)
        self.txtKhachID = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=KhachID, bg='Ghost white', width=35)
        self.txtKhachID.grid(row=0, column=1)

        self.lblTenKhach = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Tên khách hàng:", padx=2, pady=2, bg='Ghost white')
        self.lblTenKhach.grid(row=1, column=0, sticky=W)
        self.txtTenKhach = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=tenKhach, bg='Ghost white', width=35)
        self.txtTenKhach.grid(row=1, column=1)

        self.lblGioiTinh = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Giới tính:", padx=2, pady=2, bg='Ghost white')
        self.lblGioiTinh.grid(row=2, column=0, sticky=W)
        self.txtGioiTinh = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=gioiTinh, bg='Ghost white', width=35)
        self.txtGioiTinh.grid(row=2, column=1)

        self.lblNhomKhach = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Nhóm khách hàng:", padx=2, pady=2, bg='Ghost white')
        self.lblNhomKhach.grid(row=3, column=0, sticky=W)
        self.txtNhomKhach = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=nhomKhach, bg='Ghost white', width=35)
        self.txtNhomKhach.grid(row=3, column=1)

        self.lblDiaChi = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Địa chỉ:", padx=2, pady=2, bg='Ghost white')
        self.lblDiaChi.grid(row=4, column=0, sticky=W)
        self.txtDiaChi = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=diaChiKhach, bg='Ghost white', width=35)
        self.txtDiaChi.grid(row=4, column=1)

        self.lblSDTKhach = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Số điện thoại", padx=2, pady=2, bg='Ghost white')
        self.lblSDTKhach.grid(row=5, column=0, sticky=W)
        self.txtSDTKhach = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=SDTKhach, bg='Ghost white', width=35)
        self.txtSDTKhach.grid(row=5, column=1)

        self.lblEmailKhach = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Email:", padx=2, pady=2, bg='Ghost white')
        self.lblEmailKhach.grid(row=6, column=0, sticky=W)
        self.txtEmailKhach = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=emailKhach, bg='Ghost white', width=35)
        self.txtEmailKhach.grid(row=6, column=1)

        self.lblGhiChuKhach = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Ghi chú:", padx=2, pady=2, bg='Ghost white')
        self.lblGhiChuKhach.grid(row=7, column=0, sticky=W)
        self.txtGhiChuKhach = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=ghiChu, bg='Ghost white', width=35)
        self.txtGhiChuKhach.grid(row=7, column=1)

        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=12, columnspan=2, pady=45)
        #===============================================display==================================================================

        self.txtDisplay = Text(DataFrameRIGHT, height=19, width=62, bd=1, font=('arial', 11, 'bold'))
        self.txtDisplay.grid(row=0, column=0)

        #================================================ListFrame==================================================================

        lblNull = Label(ListFrame, bg='powder blue')
        lblNull.grid(row=0, column=0, pady=2)

        # header table
        lblSTT = Label(ListFrame, font=('Arial', 11, 'bold'), text='STT', padx=20, pady=2, bg='Ghost white')
        lblSTT.place(x=10, y=1)

        lblTenKhach = Label(ListFrame, font=('Arial', 11, 'bold'), text='Tên khách hàng', padx=45, pady=2, bg='Ghost white')
        lblTenKhach.place(x=85, y=1)

        lblGioiTinh = Label(ListFrame, font=('Arial', 11, 'bold'), text='Giới tính', padx=25, pady=2, bg='Ghost white')
        lblGioiTinh.place(x=293, y=1)

        lblNhomKhach = Label(ListFrame, font=('Arial', 11, 'bold'), text='Nhóm khách', padx=40, pady=2, bg='Ghost white')
        lblNhomKhach.place(x=410, y=1)

        lblDiaChi = Label(ListFrame, font=('Arial', 11, 'bold'), text='Địa chỉ', padx=75, pady=2, bg='Ghost white')
        lblDiaChi.place(x=582, y=1)
        
        lblSDTKhach = Label(ListFrame, font=('Arial', 11, 'bold'), text='SĐT', padx=40, pady=2, bg='Ghost white')
        lblSDTKhach.place(x=785, y=1)

        lblEmailKhach = Label(ListFrame, font=('Arial', 11, 'bold'), text='Email', padx=30, pady=2, bg='Ghost white')
        lblEmailKhach.place(x=901, y=1)

        lblGhiChuKhach = Label(ListFrame, font=('Arial', 11, 'bold'), text='Ghi chú', padx=24, pady=2, bg='Ghost white')
        lblGhiChuKhach.place(x=1004, y=1)

        scrollbar = Scrollbar(ListFrame)
        scrollbar.grid(row=1, column=1, sticky= 'ns')

        khachList = Listbox(ListFrame, width=122, height=9, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        khachList.bind('<<ListboxSelect>>',khachRec)
        khachList.grid(row=1, column=0, padx=8)
        scrollbar.config(command=khachList.yview)

        #================================================ButtonFrame=================================================================

        self.btnAddData = Button(ButtonFrame, text='Thêm', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=5, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text='Hiển thị', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text='Dọn dẹp', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=Clear)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Xóa', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text='Tìm kiếm', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=SearchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text='Cập nhật', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=8, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnComeBack = Button(ButtonFrame, text='Quay lại', font=('Arial', 12, 'bold'), height=1, width=14, bd=2, padx=5, command=HomeFn)
        self.btnComeBack.grid(row=0, column=6)
#////////////////////////////////////////////END KHÁCH HÀNG/////////////////////////////////////////
class HoaDon:

    def __init__(self, root):
        self.root = root
        self.root.title("Database Management Systems")
        self.root.geometry("1218x910+350+55")
        self.root.config(bg="#b3ffb3")
        
        DateIssued = StringVar()
        DateIssued.set(time.strftime('%d/%m/%Y'))
        HoaDonID = StringVar()
        NgayBan = StringVar()
        TongTriGia = StringVar()
        txtDisplay = StringVar()

        hangMuaID = StringVar()
        tenHangMua = StringVar()
        SLMua = StringVar()
        donGiaBanCTHD = StringVar()
        intSLMua = SLMua.get()
        if intSLMua != "":
            intSLMua = int(intSLMua)
        #========================================================Function========================================================
        def HomeFn():
            root.destroy()
            rootHome = Tk()
            application = Home(rootHome)
            rootHome.mainloop()

        # def CTHDFn():
        #     #root.destroy()
        #     rootCTHD = Tk()
        #     application = CTHoaDon(rootCTHD)
        #     rootCTHD.mainloop()

        def NgayBanFn():
            NgayBan.set(DateIssued.get())

        def ClearCTHD():
            hangMuaID .set('')
            tenHangMua.set('')
            SLMua.set('')
            donGiaBanCTHD.set('')

        def Cleartxt():
            HoaDonID.set('')
            NgayBan.set('')
            TongTriGia.set('')
            hangMuaID .set('')
            tenHangMua.set('')
            SLMua.set('')
            donGiaBanCTHD.set('')

        def Clear():
            Cleartxt()
            self.txtDisplay.delete('1.0', END)

        def addNew():
            DateIssued.set(time.strftime('%d/%m/%Y'))
            self.txtDisplay.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtDisplay.insert(END, 'Mã khách hàng:\t'+ HoaDonID.get()+ '\t\t\t\t' + NgayBan.get()+'\n')
            self.txtDisplay.insert(END,'=====================================================\n')
            
            self.txtDisplay.insert(END,'=====================================================')
            self.txtDisplay.insert(END,'\n\n\n\n\n\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        #====================================================DataBase Function====================================================
        #==========Hóa Đơn===========================================
        def addData():
            addNew()
            if(len(HoaDonID.get())!=0):
                management_backEnd.addHoaDonNewRec(HoaDonID.get(), NgayBan.get(), TongTriGia.get())
                HoaDonList.delete(0,END)
                HoaDonList.insert(END,(HoaDonID.get(), NgayBan.get(), TongTriGia.get()))
            Cleartxt()

        def DisplayData():
            HoaDonList.delete(0,END)
            for row in management_backEnd.viewHoaDonData():
                HoaDonList.insert(END, row)

        def HoaDonRec(event):
            global sd3 
            searchHD = HoaDonList.curselection()[0]
            sd3 = HoaDonList.get(searchHD)
            
            self.txtHoaDonID.delete(0, END)
            self.txtHoaDonID.insert(END, sd3[1])
            self.txtNgayBan.delete(0, END)
            self.txtNgayBan.insert(END, sd3[2])  
            self.txtTongTriGia.delete(0, END)
            self.txtTongTriGia.insert(END, sd3[3])
            
            self.txtDisplay.delete('1.0', END)
            self.txtDisplay.insert(END,'\t\t<==== Điện tử TÂN TÂN ====>\n\n')
            self.txtDisplay.insert(END, 'Mã khách hàng:\t'+ HoaDonID.get()+ '\t\t\t\t\t' + NgayBan.get()+'\n')
            self.txtDisplay.insert(END,'=========================================================\n')
            self.txtDisplay.insert(END,'Mã mặt hàng\t|Tên mặt hàng\t|Số lượng\t|Đơn giá \n')
            HoaDonList.delete(0,END)
            for row in management_backEnd.displayCTHDRec(HoaDonID.get()):
                self.txtDisplay.insert(END,'\n'+str(row)+'\n')
            self.txtDisplay.insert(END,'\n=========================================================')
            self.txtDisplay.insert(END,'\nTổng trị giá: '+ TongTriGia.get()+'K VNĐ')
            self.txtDisplay.insert(END,'\n\n\n\t\t\t\t\t © Nguyễn Văn Tiến')

        def deleteData():
            if(len(HoaDonID.get())!=0):
                management_backEnd.deleteHoaDonDataRec(sd3[0])
                Clear()
                DisplayData()

        def SearchData():
            HoaDonList.delete(0,END)
            for row in management_backEnd.searchHoaDonDataRec(HoaDonID.get(), NgayBan.get(), TongTriGia.get()):
                HoaDonList.insert(END, row)

        def update():
            if(len(HoaDonID.get())!=0):
                management_backEnd.deleteHoaDonDataRec(sd1[0])
            if(len(HoaDonID.get())!=0):
                management_backEnd.addHoaDonNewRec(HoaDonID.get(), NgayBan.get(), TongTriGia.get())
                HoaDonList.delete(0,END)
                HoaDonList.insert(END,(HoaDonID.get(), NgayBan.get(), TongTriGia.get()))
        #==========END Hóa Đơn===========================================

        #==========Chi tiết hóa đơn======================================
        def addDataCTHD():
            if(len(hangMuaID.get())!=0):
                management_backEnd.addCTHDNewRec(HoaDonID.get(),hangMuaID.get(), tenHangMua.get(), SLMua.get(), donGiaBanCTHD.get())
                CTHDList.delete(0,END)
                CTHDList.insert(END,(HoaDonID.get(),hangMuaID.get(), tenHangMua.get(), SLMua.get(), donGiaBanCTHD.get()))
            ClearCTHD()

        def DisplayDataCTHD():
            CTHDList.delete(0,END)
            for row in management_backEnd.viewCTHDData():
                CTHDList.insert(END, row)

        def CTHDRec(event):
            global sd2 
            searchCTHD = CTHDList.curselection()[0]
            sd2 = CTHDList.get(searchCTHD)
            
            self.txtHangMuaID.delete(0, END)
            self.txtHangMuaID.insert(END, sd2[1]) 
            self.txtHangMuaID.delete(0, END)
            self.txtHangMuaID.insert(END, sd2[2])  
            self.txtTenHangMua.delete(0, END)
            self.txtTenHangMua.insert(END, sd2[3])
            self.txtSLMua.delete(0, END)
            self.txtSLMua.insert(END, sd2[4])
            self.txtDonGiaCTHD.delete(0, END)
            self.txtDonGiaCTHD.insert(END, sd2[5])

        def deleteDataCTHD():
            if(len(hangMuaID.get())!=0):
                management_backEnd.deleteCTHDDataRec(sd2[0])
                Cleartxt()

        def SearchDataCTHD():
            CTHDList.delete(0,END)
            for row in management_backEnd.searchCTHDDataRec(HoaDonID.get(),hangMuaID.get(), tenHangMua.get(), SLMua.get(), donGiaBanCTHD.get()):
                CTHDList.insert(END, row)

        def updateCTHD():
            if(len(hangMuaID.get())!=0):
                management_backEnd.deleteCTHDDataRec(sd2[0])
            if(len(hangMuaID.get())!=0):
                management_backEnd.addCTHDNewRec(HoaDonID.get(),hangMuaID.get(), tenHangMua.get(), SLMua.get(), donGiaBanCTHD.get())
                CTHDList.delete(0,END)
                CTHDList.insert(END,(HoaDonID.get(),hangMuaID.get(), tenHangMua.get(), SLMua.get(), donGiaBanCTHD.get()))

        def tongTriGiaFn():
            a=management_backEnd.TongTriGiaRec(HoaDonID.get())
            TongTriGia.set(a)
        #==========END Chi tiết hóa đơn==================================

        #=========================================================Frames==========================================================

        MainFrame = Frame(self.root, bg="#b3ffb3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#ccffff", relief=RIDGE)
        TitFrame.pack(side=TOP, pady=5)
        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Hóa Đơn", fg="green", bg="#ccffff")
        self.lblTit.grid(row=0, columnspan=4)

        DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ListFrame = Frame(DataFrame2, bd=2, width=1300, height=210, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ListFrame.pack(side=TOP)
        ButtonFrame = Frame(DataFrame2, bd=2, width=1300, height=60, padx=18, pady=10, bg='powder blue', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='cadet blue')
        DataFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=400, padx=20, relief=RIDGE, bg='Ghost white', font=('Arial', 18, 'bold'), text='Chi tiết\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=400, padx=31, pady=3, relief=RIDGE, bg='powder blue', font=('Arial', 18, 'bold'), text='Display\n')
        DataFrameRIGHT.pack(side=RIGHT)

        #=========================================================Widget=========================================================

        self.lblHoaDonID = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Mã hóa đơn:", padx=2, pady=2, bg='Ghost white')
        self.lblHoaDonID.grid(row=0, column=0, sticky=W)
        self.txtHoaDonID = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=HoaDonID, bg='Ghost white', width=35)
        self.txtHoaDonID.grid(row=0, column=1)

        self.btnNgayBan = Button(DataFrameLEFT, font=('arial', 14, 'bold'), text="Ngày bán:", padx=2, pady=1, bg='Ghost white', command=NgayBanFn)
        self.btnNgayBan.grid(row=1, column=0, sticky=W)
        self.txtNgayBan = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=NgayBan, bg='Ghost white', width=35)
        self.txtNgayBan.grid(row=1, column=1)

        self.lblHangMuaID = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="\nChi tiết hóa đơn", padx=2, pady=2, bg='Ghost white')
        self.lblHangMuaID.grid(row=2, column=0, sticky=W)
    
        self.lblHangMuaID = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Mã hàng:", padx=2, pady=2, bg='Ghost white')
        self.lblHangMuaID.grid(row=3, column=0, sticky=W)
        self.txtHangMuaID = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=hangMuaID, bg='Ghost white', width=35)
        self.txtHangMuaID.grid(row=3, column=1)

        self.lblTenHangMua = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Tên hàng:", padx=2, pady=2, bg='Ghost white')
        self.lblTenHangMua.grid(row=4, column=0, sticky=W)
        self.txtTenHangMua = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=tenHangMua, bg='Ghost white', width=35)
        self.txtTenHangMua.grid(row=4, column=1)

        self.lblSLMua = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Số lượng mua:", padx=2, pady=2, bg='Ghost white')
        self.lblSLMua.grid(row=5, column=0, sticky=W)
        self.txtSLMua = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=SLMua, bg='Ghost white', width=35)
        self.txtSLMua.grid(row=5, column=1)

        self.lblDonGiaCTHD = Label(DataFrameLEFT, font=('arial', 14, 'bold'), text="Đơn giá:", padx=2, pady=2, bg='Ghost white')
        self.lblDonGiaCTHD.grid(row=6, column=0, sticky=W)
        self.txtDonGiaCTHD = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=donGiaBanCTHD, bg='Ghost white', width=35)
        self.txtDonGiaCTHD.grid(row=6, column=1)
        #==============================================Button CTHD===================================================================
        self.NULL = Label(DataFrameLEFT, font=('arial', 14, 'bold'), padx=2, pady=2, bg='Ghost white')
        self.NULL.grid(row=7, column=0, sticky=W)
        self.NULL = Label(DataFrameLEFT, font=('arial', 14, 'bold'), padx=2, pady=2, bg='Ghost white')
        self.NULL.grid(row=8, column=0, sticky=W)

        self.btnThoat = Button(text="Thêm", font=('arial', 12, 'bold'), bg='powder blue', height=1, width=7, command=addDataCTHD)
        self.btnThoat.place(x=115, y=450)

        self.btnThoat = Button(text="Hiển thị", font=('arial', 12, 'bold'), bg='powder blue', height=1, width=7, command=DisplayDataCTHD)
        self.btnThoat.place(x=195, y=450)

        self.btnThoat = Button(text="Xóa", font=('arial', 12, 'bold'), bg='powder blue', height=1, width=7, command=deleteDataCTHD)
        self.btnThoat.place(x=275, y=450)

        self.btnThoat = Button(text="Update", font=('arial', 12, 'bold'), bg='powder blue', height=1, width=7)
        self.btnThoat.place(x=355, y=450)

        self.btnThoat = Button(text="Tìm kiếm", font=('arial', 12, 'bold'), bg='powder blue', height=1, width=7)
        self.btnThoat.place(x=435, y=450)

        #==============================================END Button CTHD===============================================================
        self.btnTongTriGia = Button(DataFrameLEFT, font=('arial', 14, 'bold'), text="Tổng trị Giá:", padx=2, pady=2, bg='Ghost white', command=tongTriGiaFn)
        self.btnTongTriGia.grid(row=9, column=0, sticky=W)
        self.txtTongTriGia = Entry(DataFrameLEFT, font=('arial', 14, 'bold'), textvariable=TongTriGia, bg='Ghost white', width=35)
        self.txtTongTriGia.grid(row=9, column=1)

        
        txt1 = Label(DataFrameLEFT, bg='Ghost white')
        txt1.grid(row=10, columnspan=2, pady=4)
        #===============================================display==================================================================

        self.txtDisplay = Text(DataFrameRIGHT, height=20, width=65, bd=1, font=('arial', 11, 'bold'))
        self.txtDisplay.grid(row=0, column=0)

        #================================================ListFrame==================================================================

        lblNull = Label(ListFrame, bg='powder blue')
        lblNull.grid(row=0, column=0, pady=2)

        # header table

        lblHoaDonID = Label(ListFrame, font=('Arial', 11, 'bold'), text='Chi tiết hóa đơn', width=30, padx=45, pady=2, bg='Ghost white')
        lblHoaDonID.place(x=115, y=1)

        lblTriGia = Label(ListFrame, font=('Arial', 11, 'bold'), text='Hóa đơn', width=30, padx=40, pady=2, bg='Ghost white')
        lblTriGia.place(x=695, y=1)

        scrollbar = Scrollbar(ListFrame)
        scrollbar.grid(row=1, column=1, sticky= 'ns')

        CTHDList = Listbox(ListFrame, width=61, height=9, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        CTHDList.bind('<<ListboxSelect>>', CTHDRec)
        CTHDList.grid(row=1, column=0, padx=8)
        scrollbar.config(command=CTHDList.yview)

        HoaDonList = Listbox(ListFrame, width=61, height=9, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        HoaDonList.bind('<<ListboxSelect>>', HoaDonRec)
        HoaDonList.grid(row=1, column=1, padx=8)
        scrollbar.config(command=HoaDonList.yview)

        #================================================ButtonFrame=================================================================

        self.btnAddData = Button(ButtonFrame, text='Thêm', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=5, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text='Hiển thị', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=5, command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text='Dọn dẹp', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=7, command=Clear)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Xóa', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=5, command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text='Tìm kiếm', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=7, command=SearchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnComeBack = Button(ButtonFrame, text='Quay lại', font=('Arial', 12, 'bold'), height=1, width=17, bd=2, padx=5, command=HomeFn)
        self.btnComeBack.grid(row=0, column=5)
#=======================================================================================================================================
if __name__ == '__main__':
    root = Tk()
    application = HoaDon(root)
    root.mainloop()
