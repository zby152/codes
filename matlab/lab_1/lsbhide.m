%3.3 4.3  4.4

%3.3
% 读入嵌入载体
function [ ste_cover, len_total] = lsbhide( input, file, output)
cover = imread(input);
[row,col]=size(cover);
ste_cover=cover;
ste_cover = double( ste_cover) ;


%将秘密信息转换为二进制
f_id = fopen(file, 'r') ;
[ msg, len_total] = fread( f_id, 'ubit1') ;

% 判断秘密信息是否过大
[ m, n] = size( ste_cover) ;
if len_total > m* n
    error( "嵌入消息量过大, 请更换图像") ;
end

% 将秘密信息嵌入到信息载体中
p = 1;
for f2 = 1:n
    for f1 = 1:m
        ste_cover( f1, f2) = ste_cover( f1, f2) -mod( ste_cover( f1, f2) , 2) + msg( p, 1) ;
        if p == len_total
            break;
        end
        p = p + 1;
    end
    if p == len_total
        break;
    end
end

ste_cover = uint8( ste_cover) ;
imwrite( ste_cover, output) ;
subplot( 1, 2, 1) ; imshow( cover) ; title( "原始图像") ;
subplot( 1, 2, 2) ; imshow( output) ; title( "隐藏信息的图像") ;