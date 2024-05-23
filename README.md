## ESIC and PF Challan Report HR

A frappe custom addon to add option to generate ESIC report and PF Challan Report from ErpNext.

## Introduction
This useful Erpnext app is based on frappe framework and aims to automate and streamline the generation of Provident Fund (PF) Challan and Employees' State Insurance Corporation (ESIC) reports, ensuring compliance with Indian payroll regulations. The app will integrate with the existing payroll module in ERPNext, leveraging its data to produce the required reports. User can directly generate a single PF Challan in '.txt' format that can be uploaded directly to EPFO website as the file generated is in compliance with the EPFO standards for a payroll entry.

## Key Features
1)Integrated with Payroll Module:

Seamlessly integrates with the existing payroll system in ERPNext.
Automatically fetches employee and salary data necessary for PF and ESIC calculations.


2)PF Challan Generation:

Calculates PF contributions (employee and employer) based on the amount received by the employee in the Salary Slip.
It generates the PF Challan in the prescribed format required by the Employees' Provident Fund Organisation (EPFO).
The '.txt' file generated contains data of all the salary slips of a payroll entry.

3)ESIC Report Generation:

Calculates ESIC contributions (employee and employer) based on the IPN number set in the Employee.
The ESIC report generated is in the format mandated by the ESIC authorities.


4)Compliance and Validation:

Ensures all calculations adhere to the latest Indian payroll compliance standards.

5)User-Friendly Interface:

Easy to generate PF Challan in a single click along with the option to view the ESIC report inside the ErpNext before exporting it to excel.


## Usage:

PF Challan Generation:

Navigate to the submitted payroll entry created in the ErpNext. User will see a Create > Generate PF Challan.
After clicking on that, a PF challan in the compliance format will be generated and will be automatically attached to the payroll entry. This PF Challan will have the info of only those employees who have PF as earning and deduction component in the Salary Slip.
The generated PF Challan will have all the information like PF Number(set in the Employee), Employee name Basic , Employee's and Employer's (Divided) PF contribution and the Working days info.

ESIC Report Generation:

Navigate to the ESIC Report menu through awesome search bar inside ErpNext and select the payroll entry. User will see a list of employees who have salary slip in this payroll entry and has ESIC number activated in the Employee. User can directly export this data in excel and csv format.

The ESIC report will have all the required columns like IPN Number(set in the Employee), Employee Name, Basic + HRA amount and Working days info inside the report.

## Prerequisites:

User need to mention PF Number and ESIC number of the Employee in the Employee maste
User need to create all the required salary components like 'Basic', 'House Rent Allowance', 'PF (Employer's Contribution)' and 'PF (Employee's Contribution)' to get the accurate amounts inside the report.

#### License

MIT
