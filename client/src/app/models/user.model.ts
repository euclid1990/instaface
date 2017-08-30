export class UserModel {
  public agreed: boolean;

  constructor(
    public id: number,
    public name: string,
    public email: string,
    public gender: string,
    public avatar: string,
    public password: string,
    public password_confirmation: string) {
  }
}

export interface IGender {
  name: string;
  value: string;
}

export const FEMALE = 'F';

export const MALE = 'M';

export const GENDERS: Array<IGender> = [
  { name: 'Female', value: FEMALE },
  { name: 'Male', value: MALE }
];
