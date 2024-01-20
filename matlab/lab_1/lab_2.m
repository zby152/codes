A=imread('lena_color_512.tif');
subplot(331),imshow(A),title('原始图像');

B=rot90(A,-1);
subplot(332),imshow(B),title('顺时针旋转90度');

C=rot90(B,-1);
subplot(333),imshow(C),title('顺时针旋转180度');

D=rot90(A);
subplot(334),imshow(D),title('逆时针旋转90度');

E=fliplr(A);
subplot(335),imshow(E),title('左右对调');

F=flipud(A);
subplot(336),imshow(F),title('上下对调');

% G=(A);
% subplot(337),imshow(G),title('a');
% 
% H=(A,1);
% subplot(338),imshow(H),title('a');
 
I=tril(A,0);
subplot(339),imshow(I),title('a');
