import argparse
import csv
from faker import Faker

def parse_args():
    parser=argparse.ArgumentParser(description="Generating a CSV using Faker")
    parser.add_argument('--row','--row',type=int,help="enter the number of rows you want")
    parser.add_argument('--field','--field',nargs="+",help="the fields you want")
    parser.add_argument('--output','--output',help="output CSV file")
    parser.add_argument('--list',action='store_true',help="this is all availabale fields")
    args=parser.parse_args()
    
    if not args.list:
        miss=[]
        if args.row is None:
            miss.append('--row')
        if args.field is None:
            miss.append('--field')
        if args.field is None:
            miss.append('--output')
        if miss:
            parser.error(
                f"the following arguments are required when not using --list: "
                f"{', '.join(miss)}"
            )

            
    return args

def main():
    args = parse_args()
    fake = Faker()
    if args.list:
        provider=sorted(  m for m in dir(fake)if m != "seed" and not m.startswith("_") and callable(getattr(fake, m)))
        
        print ("Availabe fields")
        for p in provider:
            print("-",p)
        print("Special fields: id, number, float, boolean")
        return
    
    
    header=[]
    for fld in args.field:
        header.append(fld.lower() if fld.lower() in ['id','number','float','boolean'] else fld)
    
    
    with open(args.output ,'w',newline='',encoding='utf-8') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(header)
        for i in range(1, args.row + 1):
            r=[]
            for fld in args.field:
                fld_lower = fld.lower()
                if fld_lower =='id':
                    r.append(i)
                elif fld_lower =='number':
                    r.append(fake.random_number())
                elif fld_lower == 'boolean':
                    r.append(fake.boolean())
                elif fld_lower == 'float':
                    r.append(fake.pyfloat())
                else:
                    if not hasattr(fake, fld):
                        print(f"Error: Faker has no provider named '{fld}'")
                        return
                    r.append(getattr(fake, fld)())
            writer.writerow(r)
    print("Finished writing to " + args.output)
    # print("\nContents of", args.output)
    # with open(args.output, 'r', encoding='utf-8') as f:
    #     print(f.read())

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
