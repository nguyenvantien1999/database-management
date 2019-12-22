import sqlite3
#backEnd
#======================================================Khach Hang=============================================================================
def khachHangResult():
    con = sqlite3.connect("khachHangRecord.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS khachHangRecord(id INTEGER PRIMARY KEY , \
        KhachID text, tenKhach text, gioiTinh text, nhomKhach text, diaChiKhach text, SDTKhach text, emailKhach text, ghiChu text)')
    con.commit()
    con.close()

def addKhachHangNewRec(KhachID, tenKhach, gioiTinh, nhomKhach, diaChiKhach, SDTKhach, emailKhach, ghiChu):
    con = sqlite3.connect("khachHangRecord.db")
    cur = con.cursor()
    cur.execute('INSERT INTO khachHangRecord VALUES (NULL, ?,?,?,?,?,?,?,?)',(KhachID, tenKhach, gioiTinh, nhomKhach, diaChiKhach, SDTKhach, emailKhach, ghiChu))
    con.commit()
    con.close()

def viewKHData():
    con = sqlite3.connect("khachHangRecord.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM khachHangRecord')
    rows = cur.fetchall()
    con.close()
    return rows

def deleteKHDataRec(id):
    con = sqlite3.connect("khachHangRecord.db")
    cur = con.cursor()
    cur.execute('DELETE FROM khachHangRecord WHERE id=?', (id,))
    con.commit()
    con.close()

def searchKHDataRec(KhachID='', tenKhach='', gioiTinh='', nhomKhach='', diaChiKhach='', SDTKhach='', emailKhach='', ghiChu=''):
    con = sqlite3.connect("khachHangRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM khachHangRecord WHERE KhachID=? OR tenKhach=? OR gioiTinh=? OR nhomKhach=? OR diaChiKhach=? OR SDTKhach=? OR emailKhach=? OR ghiChu=?",\
        (KhachID, tenKhach, gioiTinh, nhomKhach, diaChiKhach, SDTKhach, emailKhach, ghiChu))
    rows = cur.fetchall() 
    con.close()
    return rows


#========================================================Hang=================================================================================
def hangResult():
    con = sqlite3.connect("hangRecord.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS hangRecord(id INTEGER PRIMARY KEY , \
        hangID text, tenHang text, DVTinh text, SoLuong text, donGiaNhap text, donGiaBan text, nhaCungCap text)')
    con.commit()
    con.close()


def addNewRec(hangID, tenHang, DVTinh, SoLuong, donGiaNhap, donGiaBan, nhaCungCap):
    con = sqlite3.connect("hangRecord.db")
    cur = con.cursor()
    cur.execute('INSERT INTO hangRecord VALUES (NULL, ?,?,?,?,?,?,?)',(hangID, tenHang, DVTinh, SoLuong, donGiaNhap, donGiaBan, nhaCungCap))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("hangRecord.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM hangRecord')
    rows = cur.fetchall()
    con.close()
    return rows

def deleteDataRec(id):
    con = sqlite3.connect("hangRecord.db")
    cur = con.cursor()
    cur.execute('DELETE FROM hangRecord WHERE id=?', (id,))
    con.commit()
    con.close()

def searchDataRec(hangID='', tenHang='', DVTinh='', SoLuong='', donGiaNhap='', donGiaBan='', nhaCungCap=''):
    con = sqlite3.connect("hangRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hangRecord WHERE hangID=? OR tenHang=? OR DVTinh=? OR SoLuong=? OR donGiaNhap=? OR donGiaBan=? OR nhaCungCap=?",\
        (hangID, tenHang, DVTinh, SoLuong, donGiaNhap, donGiaBan, nhaCungCap))
    rows = cur.fetchall() 
    con.close()
    return rows


#hangResult()
khachHangResult()