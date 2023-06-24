      program main
      implicit None
      
      integer, parameter :: KI = Selected_Int_Kind(9)
      integer, parameter :: DP = Selected_Real_Kind(r=50,p=14)
      
      Real(kind = DP)::r1=1.0_DP,r2,r3
      integer , parameter :: N = 300
      integer :: i=1
      real :: a(N), b(N), c(N), d(N)
      
      do i = 1,N
      read(*,*) a(i),b(i),d(i)
      c(i) = a(i)+b(i)+d(i)
      write(*,"(F4.2)") c(i)  !×¢ÊÍ
      end do    

      stop
      end program main