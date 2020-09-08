@echo off
set OSGEO4W_ROOT=C:\OSGeo4W
IF EXIST C:\OsGeo4W64\nul set OSGEO4W_ROOT=C:\OSGeo4W64
IF EXIST C:\OsGeo4W32\nul set OSGEO4W_ROOT="C:\OSGeo4W32
call "%OSGEO4W_ROOT%\bin\o4w_env.bat" >NUL
path %~dp0;%OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt4\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%
rem CD <path to cadastre files>
cmd.exe