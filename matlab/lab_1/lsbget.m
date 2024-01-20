function result = lsbget( output, len_total, goalfile)

ste_cover = imread( output) ;
ste_cover = double( ste_cover) ;

% 判断嵌入消息量是否过大
[m,n] = size( ste_cover) ;
frr = fopen( goalfile, "w");

%p代表提取信息的个数
p = 1;
for f2 = 1:n
    for f1 = 1:m
        if bitand( ste_cover( f1, f2) , 1) == 1
            fwrite( frr, 1, "ubit1") ;
            result( p, 1 ) = 1;
        else
            fwrite( frr, 0, "ubit1") ;
            result( p, 1 ) = 0;
        end
        if p == len_total
            break;
        end
        p = p + 1;
    end
    if p == len_total
        break;
    end
end

fclose( frr) ;