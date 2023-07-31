import subprocess
from secret.secret_man.secret_man import SecretManager as sm
import time

def clear() -> None:
    subprocess.run(['clear'])

def menu() -> None:
    clear()
    print('****************************************************' + '\n' +
          '********************** MENU ************************' + '\n' +
          '****************************************************' + '\n' +
          'list keys: ls           ***           get a key: get' + '\n' +
          'set a key: set          ***           quit: q       ' + '\n' +
          '****************************************************',
          end= '\n\n')
    
def choose(answers: tuple) -> str:
    while True:
        menu()
        choice = input('action....   ')
        choice = choice.lower()
        if choice not in answers:
            print('not a valid action')
            time.sleep(3)
        else: 
            clear()
            return choice

def main() -> None:
    answers = ('ls', 'get', 'set', 'q')
    
    while True:
        choice = choose(answers= answers)

        if choice == answers[0]: # ls
            print('List of all the keys set so far:' + '\n' +
                 f'{", ".join(sm.list_all_keys())}', end= '\n\n')
            cont= input('press any key to continue and q to quit... ')
            if cont == answers[3]:
                break
        
        elif choice == answers[1]: # get
            while True:    
                key_name = input('choose a key to get its value... ')
                try: 
                    key_val = sm.get_key(key_name)
                    print(f'{key_name}  =  {key_val}')
                except ValueError as err:
                    clear()
                    print(f'Value {key_name} generated the following code:' + '\n' +
                          f'{err}' + '\n')
                finally:
                    cont= input('press any key to continue, m for menu or q to quit... ')
                    if cont == answers[3]:
                        choice = cont
                        break
                    elif cont == 'm':
                        break                    
        elif choice == answers[2]:
            while True:
                print('Set an enviroment variable', end='\n\n')
                sm.set_key_from_prompt()
                cont= input('press any key to continue, m for menu or q to quit... ')
                if cont == answers[3]:
                        choice = cont
                        break
                elif cont == 'm':
                    break 

        if choice == answers[3]:
            clear()
            break

if __name__ == '__main__':
    main()