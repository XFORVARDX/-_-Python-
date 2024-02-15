I = imread('валера киборг.jpg');
 imhist(I);
 G = rgb2gray(I);
 Q=imadjust(G, [0 1], [], 1);
 
 Q =adapthisteq(G, 'ClipLimit', 0.5, 'NumTiles', [16 16]);
 image(Q);