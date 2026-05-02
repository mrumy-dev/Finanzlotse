import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

interface SummaryCard {
  label: string;
  value: string;
  detail: string;
  tone: 'neutral' | 'good' | 'warning';
}

interface CategorySpending {
  name: string;
  amount: number;
  budget: number;
  percent: number;
}

interface BudgetWarning {
  category: string;
  message: string;
  percent: number;
}

interface Subscription {
  merchant: string;
  amount: number;
  dueInDays: number;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  readonly summaryCards: SummaryCard[] = [
    {
      label: 'May spending',
      value: 'CHF 2,184',
      detail: 'CHF 416 below monthly plan',
      tone: 'good'
    },
    {
      label: 'Open warnings',
      value: '2',
      detail: 'Groceries and transport need review',
      tone: 'warning'
    },
    {
      label: 'Subscriptions',
      value: 'CHF 86',
      detail: '5 recurring payments detected',
      tone: 'neutral'
    }
  ];

  readonly categorySpending: CategorySpending[] = [
    { name: 'Rent', amount: 1450, budget: 1450, percent: 100 },
    { name: 'Groceries', amount: 542, budget: 600, percent: 90 },
    { name: 'Transport', amount: 168, budget: 180, percent: 93 },
    { name: 'Leisure', amount: 96, budget: 250, percent: 38 },
    { name: 'Learning', amount: 42, budget: 120, percent: 35 }
  ];

  readonly warnings: BudgetWarning[] = [
    {
      category: 'Groceries',
      message: 'CHF 58 left until the monthly limit',
      percent: 90
    },
    {
      category: 'Transport',
      message: 'Projected to exceed budget by CHF 22',
      percent: 93
    }
  ];

  readonly subscriptions: Subscription[] = [
    { merchant: 'Spotify', amount: 13.95, dueInDays: 4 },
    { merchant: 'Microsoft 365', amount: 10.90, dueInDays: 9 },
    { merchant: 'SBB Mobile', amount: 25.00, dueInDays: 14 }
  ];

  readonly recentTransactions = [
    { date: '02 May', merchant: 'Migros', category: 'Groceries', amount: -42.80 },
    { date: '01 May', merchant: 'SBB', category: 'Transport', amount: -7.20 },
    { date: '30 Apr', merchant: 'Payroll', category: 'Income', amount: 4200.00 },
    { date: '29 Apr', merchant: 'Orell Fuessli', category: 'Learning', amount: -38.50 }
  ];

  formatCurrency(value: number): string {
    return new Intl.NumberFormat('de-CH', {
      style: 'currency',
      currency: 'CHF'
    }).format(value);
  }
}
