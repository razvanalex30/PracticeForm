*** Settings ***
Library    SeleniumLibrary
Library    practice_form.PracticeForm

*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Set Window Position   ${2000}    ${0} 
    Maximize Browser Window

*** Variables ***
${url}    https://demoqa.com/automation-practice-form
${browser}    chrome
&{date_dict}    Month=May    Year=${1997}    Day=${30}
@{hobbies}    Sports    Music    Reading
&{text_boxes}    First Name=Razvan    Last Name=Alexandru    Email=razvanelul@yahoo.com
...    Mobile Number=1234567890    Current Address=Somewhere over the rainbow
${gender}    Male
${state}    Haryana
${city}    Panipat
@{subjects}    Chemistry    Maths    Computer Science
*** Test Cases ***
TestPracticeForm
    Open Browser Page
    Retrieve Text Boxes
    Insert Dob    ${date_dict}
    Retrieve Checkboxes    ${hobbies}
    Gender Selection    ${gender}
    Fill Textboxes    ${text_boxes}
    Select State    ${state}
    Select City    ${city}
    Input Subjects    ${subjects}
    Sleep    3
    Submit Close
    Close Browser
    