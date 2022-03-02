% Name
% Student ID
% Email

%% Question 1
clear all;

% Read the image
img = imread('bridge.tif');
img  = im2double(img);        % [0, 255] -> [0, 1]

% Plot the image
imshow(img);
title('bridge');

%% Question 2

%% Useful markups

% Formatting
%%
% *Bold font* * 
%%
% _ITALIC TEXT_ 

% LaTeX
%%
% $x^2+e^{\pi i}$ 

% Bullet list
%%
% 
% * ITEM1
% * ITEM2
% 
