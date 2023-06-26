      program main
      implicit None
      
      !integer, parameter :: KI = Selected_Int_Kind(9)
      !integer, parameter :: DP = Selected_Real_Kind(r=50,p=14)
      !
      !Real(kind = DP)::r1=1.0_DP,r2,r3
      !integer , parameter :: N = 300
      !integer :: i=1
      !real :: a(N), b(N), c(N), d(N)
      !
      !do i = 1,N
      !read(*,*) a(i),b(i),d(i)
      !c(i) = a(i)+b(i)+d(i)
      !write(*,"(F4.2)") c(i)  !×¢ÊÍ
      !end do 
      logical :: T = .True.
      !real :: r
      !real :: s
      !real, parameter ::pi = 3.14159
      !write(*,*) "Have a good time"
      !write(*,*)"That's not bad"
      !write(*,*)"""Marry"" isn't my name"
      !read(*,*) r
      !!s= (r**2)*pi
      !s = sqrt(r)*10
      !write(*,*) s
      !integer :: a=2,b=3
      !real:: ra=2.0,rb=3.0
      !write(*,*)b/a
      !write(*,*)rb/ra
!      type::person
!          character(len=30)::name
!          integer::age
!          real ::height
!      end type person
!      !
!      type(person) ::a
!      write(*,*)"Name:"
!      read(*,*)a%name
!      write(*,*)"Age:"
!      read(*,*)a%age
!      write(*,*)"Height:"
!      read(*,*)a%height
!      
!      write(*,200) a%name, a%age, a%height
!200   FORMAT('Name:',A10/,"Age:",I3/,"Height:",F6.2/)
!      integer:: a=100
!      write(*,100) a
!100   format(I4) 
      
      !!!!homework calculate m cm inch
!      integer, parameter :: DP = Selected_Real_Kind(r=50,p=14)
!      character(len=5) ::choice
!      real(kind=DP)::value
!      type::distance
!          real::m,cm,inch
!      end type distance
!      type(distance)::b
!          
!      read(*,*)choice
!      read(*,*)value
!      if (trim(choice) .eq. 'm')then
!          b%m = value
!          b%cm = value*10
!          b%inch = b%cm/30.48
!      else if(trim(choice) .eq. 'cm')then
!          b%cm = value
!          b%m = value/10
!          b%inch = b%cm/30.48                   
!      else if(trim(choice) .eq. 'inch')then             
!          b%inch = value
!          b%cm = value*30.48
!          b%m = b%cm/10         
!      end if
!      
!      write(*,100) b%cm,b%m,b%inch
!100   format(F,"CM",/,F,"M",/,F,"Inch")
      
      !call test1
      
      do while(T)
          call test2
      end do
      stop
      end program main