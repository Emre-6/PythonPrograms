while True:
    try:
        x=int(input())
        y=int(input())
        print(x/y)
    except(ZeroDivisionError,ValueError)as e:
        print('y cannot be 0')
    except Exception as e:
        print('Unknown Error')
        print(e)
    else:
        break
    finally:
        print('Finally Block is working')

    

    

