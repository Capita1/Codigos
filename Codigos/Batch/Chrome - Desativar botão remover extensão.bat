::Adicione "ExtensionInstallForcelist" no diretorio "HKLM\SOFTWARE\Policies\Google\Chrome\"
::[ID da extensão e ";https://clients2.google.com/service/update2/crx" no final
REG ADD HKLM\SOFTWARE\Policies\Google\Chrome\ExtensionInstallForcelist /v 1 /t REG_SZ /d fnfchnplgejcfmphhboehhlpcjnjkomp;https://clients2.google.com/service/update2/crx 
REG ADD HKLM\SOFTWARE\Policies\Google\Chrome\ExtensionInstallForcelist /v 2 /t REG_SZ /d khncfooichmfjbepaaaebmommgaepoid;https://clients2.google.com/service/update2/crx  