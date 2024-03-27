# linear regression (without numpy,tensorflow,pytorch)
# least square method
# y=bo+b1x  bo=intercept ,b1=coeff/slope
# bo=y_mean-b1*x_mean
# y_pred=bo+b1*x
#  xs = [-1, 0, 1, 2, 3, 4]
# ys = [-3, -1, 1, 2.8, 5.1, 6.9]

class LinearRegression:
    def __init__(self) -> None:
        self.coeff_= 0
        self.intercept_ = 0
        self.SSR= 0
        self.SST= 0
        self.r2score= 0


    def fit(self, x,y):
        if len(x)!=len(y):
            raise ValueError("x and y values are not ")  
        y_mean= sum(y)/len(y)
        x_mean= sum(x)/len(x)
        

        # Least Squares Method
        for i in range(len(x)):
            numerator=denominator=0
            numerator +=  ((x[i]-x_mean)*(y[i]-y_mean))  
            denominator+= ((x[i]-x_mean)**2)

             
        self.coeff_=numerator / denominator
        self.intercept_=y_mean-self.coeff_*x_mean

        y_pred=[]
        for i in range(len(x)):
            y_pred.append(self.intercept_+(self.coeff_ * x[i]))
            return y_pred

        #r2score
        for i in range(len(x)):
            self.SSR+=(y[i]-y_pred[i]**2)
            self.SST+=(y[i]-y_mean) **2

        self.r2score = 1 - (self.SSR / self.SST)

    def predict(self,x):
        y_pred=[]
        for  i in range(len(x)):
            y_pred.append(self.intercept_+(self.coeff_*x[i]))

        return y_pred
    #intitiation of linear regression

linear_model=LinearRegression()
xs = [-1, 0, 1, 2, 3, 4]
ys = [-3, -1, 1, 2.5, 5.8, 6.9]
linear_model.fit(xs,ys) #model training
# print(linear_model.coeff_)
# print(linear_model.intercept_)
print("\n",ys)
print(linear_model.predict(xs))#model prediction
print("score" ,linear_model.r2score)#model evalution

