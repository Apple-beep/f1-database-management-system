import pickle
import tabulate
import mysql.connector
import os

#MENU OPTIONS
def main():
    print("F1 Database")
    print()
    print("Are you:")
    print("1.An admin?")
    print("2. A user?")
    print('3. Exit')
    print()
    ch=int(input('Enter your choice'))
    if ch==1:
        admin_menu_options()
 
    elif ch==2:
        cust_main()
    
    elif ch==3:
        print()
        print('Thank you for using F1 Database')
        print()
        print('You have exited F1 Database')
        
        
def admin_menu_options():
    print("Do you want to:")
    print("1. Edit content")
    print("2. Display content")
    print("3. Exit")
    print()
    adch=int(input('Enter choice'))
    if adch==1:
        edit_content_menu()
    elif adch==2:
        display_content_menu()
    elif adch==3:
        main()
        
def edit_content_menu():
    print("What do you want to do?")
    print("1. Add content")
    print("2. Update content")
    print("3. Delete content")
    print("4. Exit")
    print()
    adch=int(input('Enter choice'))
    if adch==1:
        add_content()
    elif adch==2:
        update_content()
    elif adch==3:
        delete_content()
    elif adch==4:
        admin_menu_options()
    
def display_content_menu():
    print("What do you want to do?")
    print("1. Display all details on cars")
    print("2. Display all details on curcuits")
    print("3. Display all details on drivers")
    print("4. Display all details on Fastest laps")
    print("5. Display all details on Teams")#Shows the number of episodes for each show ie count
    print("6. Display all details on Winners")
    print("7. Exit")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        display_cars()
        display_content_menu()
    elif ch==2:
        display_circuits()
        display_content_menu()
    elif ch==3:
        display_drivers()
        display_content_menu()
    elif ch==4:
        display_fastestlap()
        display_content_menu()
    elif ch==5:
        display_teams()
        display_content_menu()
    elif ch==6:
        display_winners()
        display_content_menu()
    elif ch==7:
        admin_menu_options()

#EDIT FUNCTIONS
        
def add_content():
    print("1. Add content in car")
    print("2. Add content in circuits")
    print("3. Add content in drivers")
    print("4. Add content in fastestlap")
    print("5. Add content in teams")
    print("6. Add content in winners")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        add_content_car()
    elif ch==2:
        add_content_circuits()
    elif ch==3:
        add_content_drivers()
    elif ch==4:
        add_content_fastestlap()
    elif ch==5:
        add_content_teams()
    elif ch==6:
        add_content_winners()
    
def update_content():
    print("1. Update content in car")
    print("2. Update content in circuits")
    print("3. Update content in drivers")
    print("4. Update content in fastestlap")
    print("5. Update content in teams")
    print("6. Update content in winners")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        update_content_car()
    elif ch==2:
        update_content_circuits()
    elif ch==3:
        update_content_drivers()
    elif ch==4:
        update_content_fastestlap()
    elif ch==5:
        update_content_teams()
    elif ch==6:
        update_content_winners()

def delete_content():
    print("1. Delete content in car")
    print("2. Delete content in circuits")
    print("3. Delete content in drivers")
    print("4. Delete content in fastestlap")
    print("5. Delete content in teams")
    print("6. Delete content in winners")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        delete_content_car()
    elif ch==2:
        delete_content_circuits()
    elif ch==3:
        delete_content_drivers()
    elif ch==4:
        delete_content_fastestlap()
    elif ch==5:
        delete_content_teams()
    elif ch==6:
        delete_content_winners()

    
def add_content_car():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        carid=int(input('Enter CarID'))
        teamid=input('Enter TeamID')
        driverid=input("Enter DriverID") 
        engine=input('Enter Engine Type')
        weight=float(input("Enter weight"))
        aeropack=input('Enter Aerodynamics Package')
        q=f"insert into car values ({carid},'{teamid}','{driverid}','{engine}',{weight},'{aeropack}')"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_car()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()
        
def add_content_circuits():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        cirid=input('Enter CircuitID')
        cirname=input('Enter Circuit Name')
        location=input("Enter Location") 
        launch=input('Enter Launch Year')
        lapc=float(input("Enter lap count"))
        cirlen=input('Enter Circuit Length')
        q=f"insert into circuits values ('{cirid}','{cirname}','{location}','{launch}',{lapc},'{cirlen}')"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_circuits()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()

def add_content_drivers():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        driversid=input('Enter DriversID')
        teamid=input('Enter TeamID')
        carid=int(input("Enter CarID"))
        country=input('Enter country')
        podiums=int(input("Enter no of podiums"))
        points=float(input('Enter points'))
        gpenter=int(input("Enter no of Grand prix enteres"))
        wc=int(input("Enter no of world champoinships won"))
        highestfinish=input('Enter highest race finish')
        highestgrid=int(input("Enter highest grid position"))
        dob=input('Enter date of birth')
        pob=input('Enter place of birth')
        q=f"insert into drivers values ('{driversid}','{teamid}',{carid},'{country}',{podiums},{points},{gpenter},{wc},'{highestfinish}',{highestgrid},'{dob}','{pob}')"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_car()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()
        
def add_content_fastestlap():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter Grand Prix')
        driver=input('Enter driver')
        car=input("Enter car") 
        time=input('Enter time')
        q=f"insert into fastestlap values ('{gp}','{driver}','{car}','{time}')"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_car()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()
        
def add_content_winners():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter Grand Prix name')
        date=input('Enter date')
        winner=input("Enter winner") 
        points=input('Enter points')
        car=input("Enter car")
        laps=int(input('Enter laps'))
        time=input('Enter time')
        q=f"insert into winners values ('{gp}','{date}','{winner}','{points}','{car}',{laps},'{time}')"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_car()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()
        
def add_content_teams():#option ONLY FOR ADMIN to add content
#need to modify so that avg rating comes by itself 
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        teamid=input('Enter teamID')
        teamname=input('Enter Team name')
        base=input("Enter base") 
        tchief=input('Enter Team chief')
        techchief=input("Enter Technical Cheif")
        chassis=input('Enter chassis')
        powerunit=input('Enter power unit')
        firstteamentry=int(input('Enter first team entry'))
        wc=int(input("Enter world championships"))
        highracefinish=input('Enter highest race finish')
        polepositions=int(input("Enter polepositions"))
        fastestlaps=int(input('Enter fastest laps'))
        q=f"insert into teams values ('{teamid}','{teamname}','{base}','{tchief}','{techchief}','{chassis}','{powerunit}',{firstteamentry},{wc},'{highracefinish}',{polepositions},{fastestlaps})"
        mycur.execute(q)
        mycon.commit()
        print()
        print('Enter more records?')
        print()
        ch=input("Enter 'yes' or 'no'")
        if ch=='yes':
            add_content_car()
        else:
            admin_menu_options()
    except:
        print('This content ID already exists. Choose another one')
        mycur.close()
        mycon.close()
        add_content()
        
        
def update_content_car():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        carid=int(input('Enter Car ID that you want to update'))
        q=f"select * from car where carid={carid}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Car ID','Team ID','Driver ID','Engine Type','Weight','Aerodynamics Package'],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This Car ID does not exist. Try again or exit')
            ch=int(input("do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            teamid=input('Enter TeamID')
            driverid=input("Enter DriverID") 
            engine=input('Enter Engine Type')
            weight=float(input("Enter weight"))
            aeropack=input('Enter Aerodynamics Package')
            q=f"update car set teamid='{teamid}', Driverid='{driverid}',enginetype='{engine}',weight={weight},aerodynamicspackage='{aeropack}' where carid={carid}"
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()
        
def update_content_circuits():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        cirid=input('Enter circuit ID that you want to update')
        q=f"select * from circuits where circuitid='{cirid}'"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Circuit ID','Circuit Name','Location','Launch Year','Lap Count','Circuit Length'],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This Circuit ID does not exist. Try again or exit')
            ch=int(input("do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            cirname=input('Enter Circuit Name')
            location=input("Enter Location") 
            launchyear=int(input('Enter Launch Year'))
            lapc=int(input("Enter Lap count"))
            cirlen=float(input('Enter Circuit length'))
            q=f"update circuits set circuitname='{cirname}', location='{location}',launchyear={launchyear},lapcount={lapc},circuitlength={cirlen} where circuitid='{cirid}'" 
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()
    
def update_content_drivers():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        did=int(input('Enter Drivers ID that you want to update'))
        q=f"select * from drivers where driversid={did}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Drivers ID','Team ID','Car ID','Country','Podiums','Points','Grand Prix','World Championships','Highest race finish','Highest Grid Position','Date of Birth','Place of Birth'],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This drivers ID does not exist. Try again or exit')
            ch=int(input("do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            teamid=input('Enter TeamID')
            carid=int(input("Enter CarID"))
            country=input('Enter country')
            podiums=int(input("Enter no of podiums"))
            points=float(input('Enter points'))
            gpenter=int(input("Enter no of Grand prix enteres"))
            wc=int(input("Enter no of world champoinships won"))
            highestfinish=input('Enter highest race finish')
            highestgrid=int(input("Enter highest grid position"))
            dob=input('Enter date of birth')
            pob=input('Enter place of birth')
            q=f"update car set teamid='{teamid}', carid={carid},country='{country}',Podiums={podiums},Points={points}, GrandsPrixEntered={gpenter} ,WorldChampoinships={wc},Highestracefinish='{highestfinish}',HighestGridPosition={highestgrid},DOB='{dob}',PlaceofBirth='{pob}'where driversid={did}"
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()

def update_content_fastestlap():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter Grand Prix that you want to update')
        q=f"select * from fastestlap where grandprix='{gp}'"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grandprix','Driver','Car','Time'],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This grand prix does not exist. Try again or exit')
            ch=int(input("do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            driver=input('Enter driver')
            car=input("Enter car") 
            time=input('Enter time')
            q=f"update fastestlap set Driver='{driver}',car='{car}',time='{time}' where grandprix='{gp}'"
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()
        
def update_content_teams():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        teamid=input('Enter team ID that you want to update')
        q=f"select * from teams where teamid='{teamid}'"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Team ID','Base','Team Chief','Technical Chief','Chassis','Power Unit','First Team entry','World Championships','Highest race finish','Pole Positions','Fastest Laps'],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This team ID does not exist. Try again or exit')
            ch=int(input("do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            teamname=input('Enter Team name')
            base=input("Enter base") 
            tchief=input('Enter Team chief')
            techchief=input("Enter Technical Cheif")
            chassis=input('Enter chassis')
            powerunit=input('Enter power unit')
            firstteamentry=int(input('Enter first team entry'))
            wc=int(input("Enter world championships"))
            highracefinish=input('Enter highest race finish')
            polepositions=int(input("Enter polepositions"))
            fastestlaps=int(input('Enter fastest laps'))
            q=f"update fastestlap set TeamName='{teamname}', Base='{base}',TeamChief='{tchief}',TechnicalChief='{techchief}',Chassis='{chassis}',PowerUnit='{powerunit}', FirstTeamEntry={firstteamentry},WorldChampionships={wc},HighestRaceFinish='{highracefinish}',PolePositions={polepositions},FastestLaps={fastestlaps} where teamid={teamid}"
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()
        
def update_content_winnners():#option ONLY FOR ADMIN to update content
#TRY FOR EACH COLUMN IF THERE IS TIME
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter Grand Prix that you want to update')
        q=f"select * from winners where grandprix={gp}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Date','Winners','Points','Car','Laps','Time '],tablefmt='pretty'))
        print(s)
        if rs==None:
            print('This grand prix does not exist. Try again or exit')
            ch=int(input("Do you want to 1.try again or 2.exit?"))
            if ch==1:
                update_content()
            else:
                admin_menu_options()
        else:
            date=input('Enter date')
            winner=input("Enter winner") 
            points=input('Enter points')
            car=input("Enter car")
            laps=int(input('Enter laps'))
            time=input('Enter time')
            q=f"update winners set date='{date}', winner='{winner}',points='{points}',car='{car}',laps={laps},time='{time} where grandprix={gp}"
            mycur.execute(q)
            mycon.commit()
            print("Records updated!")
            print('Update more records?')
            print()
            ch=input("Enter 'yes' or 'no'")
            if ch=='yes':
                update_content()
            else:
                admin_menu_options()
    except:
        mycur.close()
        mycon.close()
        
        
def delete_content_car():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        cid=int(input('Enter car ID that you want to delete'))
        q=f"select * from car where carid={cid}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Car ID','Team ID','Driver ID','Engine Type','Weight','Aerodynamics Package'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from car where carid={cid}"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()

def delete_content_circuits():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        cirid=input('Enter circuit ID that you want to delete')
        q=f"select * from circuits where CircuitID='{cirid}'"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Circuit ID','Circuit Name','Location','Launch Year','Lap Count','Circuit Length'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from circuits where CircuitID='{cirid}'"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()

def delete_content_drivers():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        did=input('Enter drivers ID that you want to delete')
        q=f"select * from drivers where driversid={did}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Drivers ID','Team ID','Car ID','Country','Podiums','Points','Grand Prix','World Championships','Highest race finish','Highest Grid Position','Date of Birth','Place of Birth'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from drivers where driversid={did}"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()

def delete_content_fastestlap():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter grand prix that you want to delete')
        q=f"select * from fastestlap where GrandPrix='{gp}'"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Driver Name','Car','Time'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from fastestlap where GrandPrix='{gp}'"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()
    
def delete_content_teams():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        tid=input('Enter team ID that you want to delete')
        q=f"select * from teams where teamid={tid}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Team ID','Base','Team Chief','Technical Chief','Chassis','Power Unit','First Team entry','World Championships','Highest race finish','Pole Positions','Fastest Laps'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from teams where teamid={tid}"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()
    
def delete_content_winners():#Deleting content
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_Project')
        mycur=mycon.cursor()
        gp=input('Enter grand prix that you want to delete')
        q=f"select * from winners where grandprix={gp}"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Date','Winners','Points','Car','Laps','Time'],tablefmt='pretty'))
        print(s)
        ch=input("Are you sure you want to delete this item? (Enter 'y' or 'n')")
        if ch=='y':
            q=f"delete from winners where grandprix={gp}"
            mycur.execute(q)
            mycon.commit()
            print(mycur.rowcount,'Record successfully deleted')
            edit_content_menu()
        else:
            admin_menu_options()
            
    except Exception as e:
        print(e)
        mycon.rollback()
    mycur.close()
    mycon.close()
    
#SEARCH/DISPLAY FUNCTIONS
    
def display_cars():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from car"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Car ID','Team ID','Driver ID','Engine Type','Weight','Aerodynamics Package'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
    

def display_circuits():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from circuits"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Circuit ID','Circuit Name','Location','Launch Year','Lap Count','Circuit Length'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def display_drivers():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from drivers"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Drivers ID','Team ID','Car ID','Country','Podiums','Points','Grand Prix','World Championships','Highest race finish','Highest Grid Position','Date of Birth','Place of Birth'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
    
def display_fastestlap():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from fastestlap"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Driver Name','Car','Time'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
    
def display_teams():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from teams"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Team ID','Base','Team Chief','Technical Chief','Chassis','Power Unit','First Team entry','World Championships','Highest race finish','Pole Positions','Fastest Laps'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
    
def display_winners():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"select * from winners"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Date','Winners','Points','Car','Laps','Time'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def cust_main():
    print("What do you want to do?")
    print("1. Display all details on cars")
    print("2. Display all details on curcuits")
    print("3. Display all details on drivers")
    print("4. Display all details on Fastest laps")
    print("5. Display all details on Teams")
    print("6. Display all details on Winners")
    print("7. Advanced queries")
    print("8. Exit")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        display_cars()
        display_content_menu()
    elif ch==2:
        display_circuits()
        display_content_menu()
    elif ch==3:
        display_drivers()
        display_content_menu()
    elif ch==4:
        display_fastestlap()
        display_content_menu()
    elif ch==5:
        display_teams()
        display_content_menu()
    elif ch==6:
        display_winners()
        display_content_menu()
    elif ch==7:
        advanced_queries_menu()
        display_content_menu()
    elif ch==8:
        main()


def advanced_queries_menu():
    print("What do you want to do?")
    print()
    print("Set Operations Queries")
    print("1. Union of Winners and Fastest Lap Drivers")
    print("2. Intersection of Winners and Fastest Lap Drivers")
    print("3. Difference between Fastest Lap and Winners")
    print()
    print("Set Membership and Comparison Queries")
    print("4. Drivers in Multiple Teams")
    print("5. Circuits with Fastest Laps by Any Driver")
    print("6. Average Lap Time by Circuit")
    print("7. Ranking Drivers by Total Wins")
    print()
    print("Advanced Aggregate Functions Queries")
    print("8. Team Performance Summary")
    print()
    print("OLAP and Window Function Queries")
    print("9. Cumulative Points by Driver and Season")
    print("10. Rank Drivers by Average Lap Time for Each Circuit")
    print("11. DTop N Drivers by Wins")
    print("12. Comparison of Driver Points Across Seasons")
    print("13. Exit")
    
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        union()
        advanced_queries_menu()
    elif ch==2:
        intersection()
        advanced_queries_menu()
    elif ch==3:
        difference()
        advanced_queries_menu()
    elif ch==4:
        using_in()
        advanced_queries_menu()
    elif ch==5:
        using_exists()
        advanced_queries_menu()
    elif ch==6:
        using_with()
        advanced_queries_menu()
    elif ch==7:
        ranking()
        advanced_queries_menu()
    elif ch==8:
        rollup()
        advanced_queries_menu()
    elif ch==9:
        cummulative()
        advanced_queries_menu()
    elif ch==10:
        rank_avg_time()
        advanced_queries_menu()
    elif ch==11:
        top_N()
        advanced_queries_menu()
    elif ch==12:
        comparison()
        advanced_queries_menu()
    elif ch==13:
        cust_main()


def union():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT winner FROM Winners UNION SELECT driver FROM FastestLap"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Winner'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()

def intersection():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT Grandprix, winner FROM Winners INTERSECT SELECT Driver FROM FastestLap;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Winner'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def difference():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT winner FROM FastestLap EXCEPT SELECT Driver FROM Winners"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Winner'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def using_in():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT grandprix, driver FROM FastestLap WHERE driver IN (SELECT winner FROM winners)"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Grand Prix','Driver'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def using_exists():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT circuitid, circuitname FROM Circuits c WHERE EXISTS (SELECT 1 FROM FastestLap f WHERE f.grandprix = c.location);"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Circuit ID','Circuit Name'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def using_with():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"WITH AvgLapTimes AS (SELECT AVG(Time) AS avg_lap_time FROM FastestLap GROUP BY car) SELECT * FROM AvgLapTimes;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Average lap time'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def ranking():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"WITH DriverWins AS (SELECT winner, COUNT(*) AS total_wins FROM Winners GROUP BY winner), RankedDriverWins AS (SELECT winner, total_wins, ROW_NUMBER() OVER (ORDER BY total_wins DESC) AS ranking FROM DriverWins) SELECT winner, total_wins, ranking FROM RankedDriverWins;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Winner','Total wins','Ranking'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def rollup():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT c.CircuitName, f.Driver, COUNT(*) AS TotalFastestLaps FROM FastestLap f JOIN Circuits c ON f.GrandPrix = c.location GROUP BY ROLLUP(c.CircuitName, f.Driver);"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Circuit name','Driver','Count'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def cummulative():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"WITH RacePoints AS (SELECT w.Winner AS Driver, w.Points AS RacePoints, w.Date AS RaceDate FROM Winners w) SELECT Driver, RaceDate, SUM(RacePoints) OVER (PARTITION BY Driver ORDER BY RaceDate) AS CumulativePoints FROM RacePoints ORDER BY Driver, RaceDate;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Driver','Race Date','Cummulative points'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def rank_avg_time():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT f.Driver, f.GrandPrix AS Circuit, AVG(CAST(SUBSTRING_INDEX(f.Time, ':', -1) AS DECIMAL(5,2))) AS AvgLapTime, RANK() OVER (PARTITION BY f.GrandPrix ORDER BY AVG(CAST(SUBSTRING_INDEX(f.Time, ':', -1) AS DECIMAL(5,2)))) AS Ranking FROM FastestLap f GROUP BY f.GrandPrix, f.Driver ORDER BY f.GrandPrix, Ranking;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Driver','Circuit','Average Lap Time','Ranking'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def top_N():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT w.Winner AS Driver, COUNT(*) AS TotalWins FROM Winners w GROUP BY w.Winner ORDER BY TotalWins DESC LIMIT 5;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Driver','Total Wins'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()


def comparison():
    try:
        mycon=mysql.connector.connect(host='localhost',user='root',password='mysql@2022',database='C425_project')
        mycur=mycon.cursor()
        q=f"SELECT w.Winner AS Driver, YEAR(STR_TO_DATE(w.Date, '%d-%b-%y')) AS Season, SUM(w.Points) AS TotalPoints FROM Winners w GROUP BY Driver, Season ORDER BY Driver, Season;"
        mycur.execute(q)
        rs=mycur.fetchall()
        s=(tabulate.tabulate(rs,headers=['Driver','Season','Total Points'],tablefmt='pretty'))
        print(s)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()



main()

































