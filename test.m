% Read 1.jpg through m.jpg.  
% Files are in the "yourFolder" directory.
folder='mnistasjpg/testSample';
a = dir('mnistasjpg/testSample/*.jpg');
m = numel(a);
imageData = []
for k = 1:m
  jpgFilename = sprintf('img_%d.jpg', k);
  fullFileName = fullfile(folder, jpgFilename);
  if exist(fullFileName, 'file')
    imageData = [imageData imread(fullFileName)];
  else
    warningMessage = sprintf('Warning: image file does not exist:\n%s', fullFileName);
    uiwait(warndlg(warningMessage));
  end
  imshow(imageData);
end

csvwrite('testData.csv',imageData);