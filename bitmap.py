bitmap = """
  ....................................................................
     **************   *  *** **  *      ******************************
    ********************* ** ** *  * ****************************** *
   **      *****************       ******************************
            *************          **  * **** ** ************** *
             *********            *******   **************** * *
              ********           ***************************  *
     *        * **** ***         *************** ******  ** *
                 ****  *         ***************   *** ***  *
                   ******         *************    **   **  *
                   ********        *************    *  ** ***
                     ********         ********          * *** ****
                     *********         ******  *        **** ** * **
                     *********         ****** * *           *** *   *
                       ******          ***** **             *****   *
                       *****            **** *            ********
                      *****             ****              *********
                      ****              **                 *******   *
                      ***                                       *    *
                    **     *                    *
  ....................................................................
"""

message = 'ZOV'

if len(message) == 0:
    print('Message is empty')
else:
    bitmap_list = list(bitmap)
    message_index = 0

    for i in range(len(bitmap_list)):
        if bitmap_list[i] == '*':
            bitmap_list[i] = message[message_index]
            message_index = (message_index + 1) % len(message)

    print(''.join(bitmap_list))