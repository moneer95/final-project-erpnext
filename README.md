## Erp Gsg
1- In Journal Entry in field Entry Type Hide or Remove Options “Inter Company Journal Entry” and “Deferred Expense” .

2- In Payment Entry make Series = ‘GSG-JV-.YYYY.-’ for every New Payment Entry Created .

3- Add Purchase Taxes and Charges Template 16 % On Net Total and included in Basic Rate and make it default . 
add Sales Taxes and Charges Template 16 % On Net Total and included in Basic Rate and make it default . 

4- when submitting Material Request  with values Purpose “Material Issue” , Target Warehouse and Items   Create new Stock Entry with Stock Entry Type “Material Issue”,  Target Warehouse and Items , also add value name material request to field material_request in Items .

5-  Add field “Sales order time” to Sales order and make it Mandatory .

6- add filter “From Time”  and “To Time” and make it Mandatory to report Sales Order Analysis and use field “Sales order time” in Sales order to filter result  .

7 - Create Sales Invoice Format name sales_invoice_gsg .

8 - QR Code Image Show text
 “customer : Dwane Clark , Total : $220.00” .

9 -  Add Salary Component Earning  “Housing Allowance GSG”  with Abbr HGSG .

10 - Add Fields Check In and Check Out To Attendance .

11 - Create script report name “Attendance Working Hours” with filters “From Date”, “To Date”, “Employee” and “Department” with columns Attendance Date, Employee , Employee Name , Check in and Check Out .

12-  In report Attendance Working Hours  add  column Working Hours after column Check Out and calculate value Working Hours in report , if attendance does not have check out or check out make Working Hours zero .

13-  In report Attendance Working Hours  add  column “View Attendance“ after column  Working Hours  when user click on View Attendance will open attendance form in new tab browser .

14 - Add Form Employee Excuse application and have fields Employee , Employee Name, Department , Excuse Date , From Time, To Time, Hours and Reason .
15 - add field “Excuse Hours ALowed” to Department .
16- when saving Excuse application calc Hours and must be less than  value “Excuse Hours ALowed”  in one Month “Current Month” and from time must be before to time .

17- Create Form “To Whom It Concerns” with fields Employee , Employee Name, Department,  Date of Joining and Salary , when user  select Employee get Employee Name, Department and  Date of Joining from employee also get Salary From Last Salary Slip For Same Employee .
18- add link for  Employee Excuse application ,  Attendance Working Hours  and To Whom It Concerns to Workspace HR 
19-  Create Print Format name “Employee Format GSG” with same Design attached .


20 - Download Any Template with files  Html Css JS Img  for website  And make it default page for every site .

#### License

MIT
