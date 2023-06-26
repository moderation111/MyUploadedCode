subroutine test1
    implicit none
    integer, parameter:: KI=Selected_Int_Kind(9)
    integer, parameter:: DP=Selected_Real_Kind(r=50,p=14)
    integer(kind=KI)::rain, windspeed
    logical(4)::r,w
    write(*,*)"Rain:"
    read(*,*)rain
    write(*,*)"Windspeed:"
    read(*,*)windspeed
    
    r = (rain>500)
    w = (windspeed>=10)
    
    if (r.or.w)then
        write(*,*)"停止上班上课"
        
    else
        write(*,*)"正常上班上课"
        
    end if     
    end subroutine test1
    
subroutine test2
implicit none
integer ,parameter:: KI= Selected_Int_Kind(9)
integer , parameter::DP=Selected_Real_Kind(r=50,p=14)
integer(kind=KI) ::score
character(3) :: grade
write(*,*) "Score:"
read(*,*) score

if(score>=90 .and. score<=100)then
    grade = 'A'
    
else if (score>=80 .and. score <90)then
    grade = 'B'
else if (score>=70 .and. score <80)then
    grade = 'C'
else if (score >=60 .and. score <70)then
    grade = 'D'
else if (score >=0 .and. score <60)then
    grade = "bad"
else
    grade = '?'
end if

write(*,100) grade
100 format("Grade:",A3)   
    
end subroutine test2
    