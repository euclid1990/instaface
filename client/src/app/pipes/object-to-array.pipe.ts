import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'objectToArray'
})
export class ObjectToArrayPipe implements PipeTransform {

  transform(value: Object, keyName: string = 'key', isSort: boolean = false): Object[] {
    const keyArr: Array<any> = Object.keys(value);
    let dataArr: Array<any> = [];
    keyArr.forEach((key: any) => {
      let t: Array<any> = [];
      if (value[key] instanceof Array) {
        t = value[key];
      } else {
        t.push(value[key]);
      }
      t[keyName] = key;
      dataArr.push(t);
    });
    if (isSort) {
      dataArr.sort((a: Object, b: Object): number => {
        return a[keyName] > b[keyName] ? 1 : -1;
      });
    }
    return dataArr;
  }

}
