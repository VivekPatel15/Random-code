public class AppleRiddle{

     public static void main(String []args){
      for(int i = 0; i < 100001; i++){
          int i2 = i%2;
          int i3 = i%3;
          int i4 = i%4;
          int i5 = i%5;
          int i6 = i%6;
          int i7 = i%7;
          int i8 = i%8;
          int i9 = i%9;
          int i10 = i%10;
          int i11 = i%11;
         if(i2 == 1 && i3 == 1 && i4 == 1 && i5 == 1 && i6 == 1 && i7 == 1 &&
                i8 == 1 && i9 == 1 && i10 == 1 && i11 == 0){
             System.out.println(i);
         }
        }
     }
}