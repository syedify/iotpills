   M S B A M L   `   `   `  ����G  CHackathonApp, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null+clr-namespace:HackathonAppHackathonApp  5   	       HackathonApp.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   ,localclr-namespace:HackathonApp     5   	     � Title$  
MainWindow��5   	   $	��350��6   $	��525��6)   .��5	      � ��5
   
   �� 5       �� ImageSource$* $C:/Users/Owner/Pictures/Pharmacy.jpg��6    j� Stretch$ UniformToFill=�6L    �� Opacity$
 0.20Q�6d    � ColumnDefinitions 5   
   �� 5      $��* �6   �� 5      $��* �6   �� 5      $��* �6    � RowDefinitions 5   
   �� 5      $��* �6   �� 5      $��* �6   �� 5      $��* �6   �� 5      $��* �6   �� 5      $��* �6   �� 5      $��* �6   .+�5   
   �� $��20(�6   $
��Bold"�6"   $��Center=�64   $��Center=�6Q   $��0��6m   $��0��6z   Patient Name :6�   �� 5   
   -   5        $��textbox1��5       $��20(�6   $��Center=�60   $��1��6M   $��0��6]   $��30��6k   $	��150��6w   �� 5   
   $��20(�6   $
��Bold"�6"   $��Center=�64   $��Center=�6Q   $��1��6m   $��0��6z   Doctor Name :6�   �� 5   
   -   5        $��textbox2��5       $��20(�6   $��Center=�60   $��1��6M   $��1��6]   $��30��6k   $	��150��6x   �� 5   
   $��20(�6   $
��Bold"�6"   $��Center=�64   $��Center=�6Q   $��2��6m   $��0��6z   
Quantity :6�   �� 5   
   -   5        $��textbox3��5       $��20(�6   $��Center=�60   $��1��6M   $��2��6]   $��30��6k   $	��150��6x   �� 5    
   $��20(�6   $
��Bold"�6"   $��Center=�64   $��Center=�6Q   $��3��6m   $��0��6z   	Refills :6�   �� 5!   
   -   5        $��textbox4��5!       $��20(�6   $��Center=�60   $��1��6M   $��3��6]   $��30��6k   $	��150��6x   �� 5"   
   $��20(�6   $
��Bold"�6#   $��Center=�65   $��Center=�6R   $��4��6n   $��0��6{   Day Supply :6�   �� 5#   
   -   5        $��textbox5��5#       $��20(�6   $��Center=�60   $��1��6M   $��4��6]   $��30��6k   $	��150��6x   �� 5&   
   -   5        $��Center=�5&      $��1��6/   $��5��6?   $��30��6N   $	��100��6Z   $
��Send��6f   6u   5'      5(      