   M S B A M L   `   `   `  ����K  GBootleg CCleaner, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null3clr-namespace:Bootleg_CCleanerBootleg_CCleaner  5   	   !    Bootleg_CCleaner.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   0localclr-namespace:Bootleg_CCleaner     5   	     � Title$  
MainWindow��5   	   $��408.75��6   $��582.5��6,    � WindowStyle$
 None=�6:    � AllowsTransparency . .��5	      � -   5         �Name$ 	Main_Grid��5	      
�������.+�5
   
   � $
��Left=�6   $	��154��6*   ���	#FFA6BAFF.+�5      �� $��31��6   $��
10,10,10,0q�6$   $
��Wrap=�68   $��Bootleg CCleaner��6L   $	��Top=�6d   ��5      �� 5       �� Color# � ��6&   5      �� 5      -   5         ��Name$ Presets_TextBlock��5      $��20��63   $��
10,46,10,0q�6?   $
��Wrap=�6S   $��Presets��6g   $	��Top=�6v   ���	#FFA6BAFF��5      �� 5      $ White��6&   5      �� 5      -   5        $ Paths_TextBlock��5      $��20��61   $��
10,71,10,0q�6=   $
��Wrap=�6Q   $��Paths��6e   $	��Top=�6r   
����������	#FFA6BAFF6�   �� 5      -   5        $ Cleanup_TextBlock��5      $��20��63   $��
10,96,10,0q�6?   $
��Wrap=�6S   $��Cleanup��6g   $	��Top=�6v   
����������	#FFA6BAFF6�   5      �� 5   
   -   5         ��Name$ Close_Button��5      $�� ��6'   $��40��62   $	��Top=�6>   $��0q�6V   $��Right=�6j   $��50��6�   ��5      �� 5       �� ImageSource$ Close Icon.png��6    j� Stretch$
 None=�6:   5      �� 5   
   -   5        $ Maximize_Button��5      $�� ��6*   $��40��65   $��0,0,50,0q�6A   $	��Top=�6S   $��1q�6k   $��0q�6w   $��Right=�6�   $��50��6�   ��5      �� 5      $ Maximize Icon.png��6   $
 None=�6=   5!      �� 5"   
   -   5        $ Minimize_Button��5"      $�� ��6*   $��40��65   $��	0,0,100,0q�6A   $	��Top=�6T   $��0q�6l   $��Right=�6�   $��50��6�   ��5#      �� 5$      $ Minimize Icon.png��6   $
 None=�6=   5&      �� 5'      -   5        $ Headline_Text��5'      $��33��6)   $��169,45,143,0q�65   $
��Wrap=�6K   $��Presets��6_   $	��Top=�6n   $��20(�6�   �� 5(      -	   5        	 ��Name$	 Scroll_Grid��5(      $��169,83,10,10q�6*   .��5)   
   � -
   5        $ Viewing_Grid��5)      $	��374��6%   5*      5+   	   5,      5-      